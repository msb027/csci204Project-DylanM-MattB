"""
This class will perform simple stats calcuations on our data
Most of these will be static methods
"""

from sort import *
from heap import *


class Stats:


    def __init__(self):
        pass

    @staticmethod
    def findFreqDic(aList):
        """
        Takes in a list of words, returns a dictionary of words/freq
        """
        pass

    @staticmethod
    def topNSort(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the highest freq
        """
        pass

    @staticmethod
    def bottomNSort(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the lowest freq
        """
        pass


    @staticmethod
    def topNHeap(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the highest freq
        """
        pass

    
    @staticmethod
    def bottomNHeap(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the lowest freq
        """
        pass



def testStats():
    """
    Can be used to test methods in the Stats Class
    """
    pass


if __name__ == "__main__":
    testStats()
