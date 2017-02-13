"""
Class that will contain a document (Basic unit -- "Primary Data-Structure)
"""

form util import *
from sentence import *


class Document:
    
    def __init__(self, toInfo = None, fromInfo = None, data=None):
        self.__sentences = []
        self.__sCount = -1 #Number of sentences
        self.__toInfo = toInfo #Who was the document to
        self.__fromInfo = fromInfo #Who was the document from
        self.__date = date
        self.__fwd = False
        self._reply = False


    def __getitem__(self, index):
        return self.__sentences[index]

    def __setitem__(self, index, value):
        self.__sentence[index] = value

    def getSCount(self):
        #fill me (we should not have to ever set sCount)
        pass

    def setToInfo(self, value):
        #fill me
        pass

    def getToInfo(self):
        #fill me
        pass

    def setFromInfo(self, value):
        #fill me
        pass

    def getFromInfo(self):
        #fill me
        pass
    
    
    def setDate(self, year, month, day):
        #should use date object in python timedate package
        # mydate = timedate.date(year,month, day)
        #fill me
        pass

    def getDate(self):
        #returns year,month,day
        pass


    def setFwd(self, value):
        #fill me 
        pass

    def getFwd(self):
        #fill me
        pass

    def setReply(self,value):
        #fill me
        pass
    
    def getReply(self):
        #fill me 
        pass




def testDocument():
    """
    Used to test your Document Class
    """
    pass


if __name__ == "__main__":
    testDocument()





    
