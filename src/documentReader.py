"""
Names: Dylan Mendelowitz and Matt Brown
Class used to read a document.
Each document will be product by one instance of a DocumentReader

IF DATA IS MISSING, will be noted at ??? in the file
"""

#Will be used when we find an exceptions
from userExceptions import *
#All documents contain multiple sentences
from sentence import *
#Will produce a document
from document import *


class DocumentReader:
    """
    Used to read in a document
    """

    def __init__(self, fname = ""):
        self.__fname = fname
        self.__fileRef = None #Will store the reference to file when open


    def getFName(self): #getter with extra arg?
        return self.__fname

    def setFName(self, fname): #unsure if function was supposed to be getter or setter; wrote both
        self.__fname = fname


    def __openFile(self):
        """
        Private function used to open the file and test if it exists
        """
        self.__fileRef = open(self.__fname,'r')


    def readFile(self):
        """
        Will open (if not already open)/read the file
        Make a Document and return
        If any Error, throws error
        Format of file is MIME EMAIL
        """
        self.checkFileFormat()
        newDoc = Document()
        monthList = ['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul','Aug','Sep','Oct','Nov','Dec']
        inBody = False
        sentenceCount = 0
        if self.__fileRef == None:
            self.__openFile()
        lines = self.__fileRef.readlines()
        self.__fileRef.close()
        for line in lines:
            if line[0:5] == 'Date:':
                 lineSplit = line.split()
                 day = lineSplit[2]
                 month = (monthList.index(lineSplit[3]) + 1)
                 year = lineSplit[4]
                 newDoc.setDate(year,month,day)

            elif line[0:5] == 'From:':
                lineSplit = line.split()
                newDoc.setFromInfo(lineSplit[1])

            elif line[0:3] == 'To:':
                lineSplit = line.split()
                newDoc.getToInfo(lineSplit[1].rstrip(','))

            elif '-- Forwarded' in line:
                newDoc.setFwd = True

            elif line[0:12] == 'Subject: Re:':
                newDoc.setReply = True

            elif line[0:11] == 'X-FileName:':
                isBody = True

            elif isBody == True and (('--Forwarded' in line) or ('--Original' in line)):
                isBody = False

            elif isBody == True:
                sentences = line.replace('?','.')
                sentences = sentences.replace('!','.')
                sentences = sentences.split('.')
                for sentence in sentences:
                    newDoc[sentenceCount] = Sentence(sentence)
                    sentenceCount += 1

        return newDoc

    def checkFileFormat():
        """
        Will open the file (if not already open)
        Will test if it is a correctly formatted MIME EMAIL
        """
        if self.__fileRef == None:
            self.__openFile()
        lines = self.__fileRef.readlines()
        if 'Mime-Version: 1.0' not in lines:
            raise OurInFileException
        else:
            pass



def testDocumentReader():
    """
    Used to test your DocumentReader class
    """
    pass


if __name__ == "__main__":
    testDocumentReader()
