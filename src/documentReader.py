"""
Class used to read a document.
Each document will be product by one instance of a DocumentReader

IF DATA IS MISSING, will be noted at ??? in the file 
"""

#Will be used when we find an exceptions
from user_exceptions import *
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

    
    def getFName(self, fname):
        pass

    
    def __openFile(self):
        """
        Private function used to open the file and test if it exists
        """
        pass
    
    def readFile(self):
        """
        Will open (if not already open)/read the file
        Make a Document and return
        If any Error, throws error
        Format of file is MIME EMAIL
        """
        pass

    def checkFileFormat():
        """
        Will open the file (if not already open)
        Will test if it is a correctly formatted MIME EMAIL
        """
        pass



def testDocumentReader():
    """
    Used to test your DocumentReader class
    """
    pass


if __name__ == "__main__":
    testDocumentReader()
