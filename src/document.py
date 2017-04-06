"""
Names: Dylan Mendelowitz and Matt Brown
Class that will contain a document (Basic unit -- "Primary Data-Structure)
"""

from util import *
from sentence import *
from datetime import *


class Document:

    def __init__(self, toInfo = None, fromInfo = None, date=None):
        self.__sentences = []
        self.__sCount = -1 #Number of sentences
        self.__toInfo = toInfo #Who was the document to
        self.__fromInfo = fromInfo #Who was the document from
        self.__date = date
        self.__fwd = False
        self.__reply = False


    def __getitem__(self, index):
        return self.__sentences[index]

    def __setitem__(self, index, value):
        self.__sentence[index] = value
        if self.__sCount == -1: #Not sure where else to incrememt .__sCount; no setter
            self.__sCount = 1
        else:
            self.__sCount += 1

    def getSCount(self):
        return self.__sCount


    def setToInfo(self, value):
        self.__toInfo = value


    def getToInfo(self):
        return self.__toInfo

    def setFromInfo(self, value):
        self.__fromInfo = value

    def getFromInfo(self):
        return self.__fromInfo


    def setDate(self, year, month, day):
        #should use date object in python datetime package
        # mydate = datetime.date(year,month, day)
        self.__date = datetime.date(year,month,day)


    def getDate(self):
        return self.__date


    def setFwd(self, value):
        self.__fwd = value

    def getFwd(self):
        return self.__fwd

    def setReply(self,value):
        self.__reply = value

    def getReply(self):
        return self.__reply



def testDocument():
    """
    Used to test your Document Class
    """
    pass


if __name__ == "__main__":
    testDocument()






