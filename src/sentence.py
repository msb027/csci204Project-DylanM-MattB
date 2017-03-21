"""
Names: Dylan Mendelowitz and Matt Brown
A primary data-structure.
Document will keep a list of these.
A Sentence is NOT a line.
"""

class Sentence:

    def __init__(self, sString = ""):
        self.__sString = sString
        self.__wCount = -1
        self.__endP = "" #Ending puncuation

    def getWCount(self):
        """
        If found return/else calcuate and return
        """
        if self.__wCount == -1:
            self.__wCount = len(self.__sString.split())
        else:
            return self.__wCount


    def getSString(self):
        '''Returns value of sString for the current string object'''
        return self.__sString


    def setSString(self, value):
        '''Sets the value of sString'''
        self.__sString = value

def testSentence():
    """
    Used to test your Sentence class
    """
    pass


if __name__ == "__main__":
    testSentence()


