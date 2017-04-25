"""
Names: Dylan Mendelowitz and Matt Brown
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
    '''makes the 2D List that is the xData for training the tree'''
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
    '''determines the most and least common 10 words across the training docs'''
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
        self.__yData
        self.train(self.__xData,self.__yData,self.__maxHeight)
        self.eval(self.__xData)


    def train(self, xData, yData, maxDepth):
        """
        External interface for building the tree
        """
        pass
    
    def split(self):
        '''splits the 2D list based off of whichever attribute has the lowest entropy'''
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
        
        '''
        This will take the xData for the eval docs and walk the tree following 
        the data in each node, matching it to the attributes of the eval docs based
        off of the index stored in key.When it reaches the sender attribute, 
        it will use the data it has trainedand the walk through the tree to 
        return the sender data that is stored in that node in the tree, resulting 
        in a predicition for the sender.
        '''

    
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
        
        '''The rest of this code could be solved by finding the minimum entropy
        in the xData. Then the code would call split to split on the attribute
        with the min entropy. This would become a level in the tree with each
        node storing the index that it came from in the xData as the key, and
        the actual value of the attribute would be stored as the data. The rows
        associated with each node would then have to get split again to create
        the next level of the tree. This is where we got stuck because we 
        were having trouble comprehending how to make the node and link it without
        knowing the values of the next node.
        '''
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
