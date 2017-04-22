"""
This is the file that contains your dicision tree
"""

from stats import Stats
import math


class DTreeNode:
    """
    Your Node Class for your decision tree
    """
    
    def __init__(self, key, data=None, children = None):
        """
        I am allowing these to be public to manipulate them more easily
        """
        self.key = key
        self.data = data
        self.children = children
        

def makeXData(trainDocs):
    xData = []
    names = {}
    dates = {}
    top10, bottom10 = findTopBottom10(trainDocs)
    for doc in trainDocs:
        xData.append(doc.getAttributes(top10,bottom10))
    
    countName = 0
    countDate = 0
    for row in xData:
        if row[1] not in names:
            names[row[1]] = countName
            countName += 1
        if row[2] not in names:
            names[row[2]] = countName
            countName += 1
        if row[0] not in dates:
            dates[row[0]] = countDate
            countDate += 1
        row[1] = names[row[1]]
        row[2] = names[row[2]]
        row[0] = dates[row[0]]
        
    entropyVals = []
        for i in range(len(row[0])):
            entropyVals = [entropy(i)]
        
    xData.append(entropyVals)
    
    return xData, names, dates
    
def findTopBottom10(trainDocs):
    allwords = []
    for doc in trainDocs:
        for s in range(doc.getSCount()):
            allwords.append(doc[s].split())
    freqDic = Stats.findFreqDic(allwords)
    top10 = Stats.topNSort(freqDic,10)
    bottom10 = Stats.bottomNSort(freqDic,10)
    return top10, bottom10

class MyDecisionTree:
    """
    Will contain your deicision tree algorithm
    """
    
    def __init__(self,trainDocs,evalDocs):
        self.__myRoot = DTreeNode(None,None,[])
        self.__maxHeight = -1
        self.__minHeight = -1
        self.__xData, self.__names, self.__dates = makeXData(trainDocs)


    def train(self, xData, yData, maxDepth):
        """
        External interface for building the tree
        """
        pass
    
    def split(self):
        
        minEntropy = min(self.__xData[-1])
        minEntropyIndex = self.__xData[-1].index(minEntropy)
        splitLists = {}
        keys = []
        listData = []
        for row in self.__xData[:-1]:
            newKey = row.pop(minEntropyIndex)
            if newKey not in splitLists:
                splitLists[newKey] = [row]
            else:
                splitLists[newKey].append(row)
        
        for x in splitLists:
            keys.append(x)
            listData.append(splitLists[x])
            
        return keys, listData
            
        
        


    def eval(self, xData):
        """
        External interface for evaluating the tree (Predicting)
        """
        pass
    #got Stuck

    
    def __recursiveBuild(self, root, xData, yData, maxDepth):
        """
        Where you really will build the tree
        """
        
        #Base Case
        if len(self.__xData[0]) == 1:
            for x in self.__xData:
                root.children.append(DTreeNode(x))
            return self.__myRoot
        
        keys, listData = split()
        
        for x in keys:
            
            root.children.append(DTreeNode(x,None,__recursiveBuild(newNode,xData)
        
        #Got stuck here
    
    def entropy(self,col):
        '''Calculate the entropy of each row'''
        entropyVal = 0
        column = [row[col] for row in self.__xData]
        myDict = {}
        for x in column:
            if x not in myDict:
                myDict[x] = 1
            else:
                myDict[x] += 1
        
        for x in myDict:
            p = myDict[x]//len(row)
            entropyVal += (-1 * p)*math.log2(p)
        
        return entropyVal



def testMyDecisionTree():
    """
    Used for your testing
    """
    pass


if __name__ == "__main__":
    testMyDecisionTree()
