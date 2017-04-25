"""
Names: Dylan Mendelowitz and Matt Brown
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
        freqDict = {}
        for word in aList:
            if word in freqDict:
                freqDict[word] += 1
            else:
                freqDict[word] = 1
        return freqDict

    @staticmethod
    def topNSort(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the highest freq
        """
        sortedKeys = sorted(aDic,key=aDic.get,reverse=True)
        sortedValues = sorted(aDic.values(),reverse=True)
        result = {}
        for i in range(n):
            result[sortedKeys[i]] = sortedValues[i]
        return result

    @staticmethod
    def bottomNSort(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the lowest freq
        """
        sortedKeys = sorted(aDic,key=aDic.get)
        sortedValues = sorted(aDic.values())
        result = {}
        for i in range(n):
            result[sortedKeys[i]] = sortedValues[i]
        return result


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
    words = ["test","test","test","test2","test2","test3","whatever","blah"]
    d = Stats.findFreqDic(words)
    print(d)
    print(Stats.topNSort(d,3))
    print(Stats.bottomNSort(d,3))


if __name__ == "__main__":
    testStats()
