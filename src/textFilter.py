"""
This class will filter the information inside a Document
and return a filtered (SAME) Document.
"""


from document import *


class TextFilter:
    """
    Applies a list of filter to a document and returns same filtered Document
    """
    def __init__(self, filterList=None, doc=None):
        self.__filterList = filterList
        self.__doc = doc

    def setFilterList(self, filterList):
        self.__filterList = filterList

    def setDoc(self, doc):
        self.__doc = doc

    def apply(self, doc=None):
        """
        doc is the Document we are applying each filter in the filterlist to
        """
        if doc != None:
            self.setDoc(doc)
        for aFilter in self.__filterList:
            if aFilter == "normalizeWhiteSpace": self.normalizeWhiteSpace()
            elif aFilter == "normalizeCase": self.normalizeCase()
            elif aFilter == "stripNull": self.stripNull()
            elif aFilter == "stripNumbers": self.stripNumbers()
            elif aFilter == "stripFiles": self.stripFiles()

    def normalizeWhiteSpace(self):
        for i in range(self.__doc.getSCount()):
            temp = self._doc[i].split()
            temp = " ".join(temp)
            self._doc[i] = temp

    def normalizeCase(self):
        for i in range(self.__doc.getSCount()):
            self._doc[i] = self._doc[i].lower()
    
    def stripNull(self):
        toRemove = []
        for i in range(self._doc.getSCount()):
            for ch in self._doc[i]:
                if not ch.isdigit() and not ch.isalpha():
                    toRemove.append(ch)
            for ch in toRemove:
                self._doc[i] = self._doc[i].replace(ch,"")

    def stripNumbers(self):
        for i in range(self.__doc.getSCount()):
            for num in range(10):
                self._doc[i] = self._doc[i].replace(str(num),"")
            
    def stripFiles(self):
        file = open("stripfile.txt","r")
        words = file.readlines()
        for i in range(self._doc.getSCount()):
            for word in words:
                self._doc[i] = self._doc[i].replace(word,"")
            

def testTestFilter():
    """
    Put your test for the filter class here
    """
    pass


if __name__ == "__main__":
    testTestFilter()





