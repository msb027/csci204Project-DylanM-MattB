"""
Will be used to make a decision tree using sklearn
More details will be added to this later
"""

import math
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from stats import Stats


class SKTree:
    
    def __init__(self,trainDocs,evalDocs):
        """
        More information will be given about this later
        """
        self.__trainDocs = trainDocs
        self.__evalDocs = evalDocs
        self.__names = {}
        self.__dates = {}
        self.__top10 = {}
        self.__bottom10 = {}
        self.__forward = {True:1, False:0}
        self.__reply = {True:1, False:0}
        self.__xData = []
        self.__yData = []
        self.__evalXData = []
        self.readDocs()
        self.createXData()
        self.createYData()
        self.__tree = None
        self.train(self.__xData,self.__yData,4)
        self.eval(self.__evalXData)
        self.__evalYData = self.eval(self.__evalXData)
        
    def getPrediction(self):
        return self.__evalYData
    
    def getTopBottom(self):
        '''determines the top and bottom ten most common words in the documents '''
        allwords = []
        for doc in self.__trainDocs:
            for s in range(doc.getSCount()):
                allwords.append(doc[s].split())
        for doc in self.__evalDocs:
            for s in range(doc.getSCount()):
                allwords.append(doc[s].split())
        freqDic = Stats.findFreqDic(allwords)
        top10 = Stats.topNSort(freqDic,10)
        bottom10 = Stats.bottomNSort(freqDic,10)
        count = 0
        for word in top10:
            self.__top10[word] = count
            count += 1
        for word in bottom10:
            self.__bottom10[word] = count
            count += 1
    
    def readDocs(self):
        '''pulls necessary attributes from the documents. '''
        nameCount = 0
        dateCount = 0
        self.getTopBottom()
        for doc in self.__trainDocs:
            
            if doc.getToInfo() not in self.__names:
                self.__names[doc.getToInfo()] = nameCount
                nameCount += 1
            if doc.getFromInfo() not in self.__names:
                self.__names[doc.getFromInfo()] = nameCount
                nameCount += 1
            
            if doc.getDate() not in self.__dates:
                self.__dates[doc.getDate()] = dateCount
                dateCount += 1
                
        for doc in self.__evalDocs:
            if doc.getToInfo() not in self.__names:
                self.__names[doc.getToInfo()] = nameCount
                nameCount += 1
    
    def createXData(self):
        '''Generates the 2D List that is the xData'''
        #[dates,recipients,forward,reply,numWords,top10,bottom10]
        dates = []
        recipients = []
        forward = []
        reply = []
        numWords = []
        top10 = []
        bottom10 = []
        for doc in self.__trainDocs:
            dates.append(self.__dates[doc.getDate()])
            recipients.append(self.__names[doc.getToInfo()])
            forward.append(self.__forward[doc.getFwd()])
            reply.append(self.__reply[doc.getReply()])
            words = 0
            hasTop10 = False
            hasBottom10 = False
            for s in range(doc.getSCount()):
                sentencewords = doc[s].split()
                for word in sentencewords:
                    if word in self.__top10:
                        hasTop10 = True
                    if word in self.__bottom10:
                        hasBottom10 = True
                if hasTop10:
                    top10.append(1)
                else:
                    top10.append(0)
                if hasBottom10:
                    bottom10.append(1)
                else:
                    bottom10.append(0)
                words += len(sentencewords)
            numWords.append(words)
        self.__xData = [dates,recipients,forward,reply,numWords,top10,bottom10]
    
    def createYData(self):
        for doc in self.__trainDocs:
            self.__yData.append(self.__names[doc.getFromInfo()])
    
    def createEvalXData(self):
        '''makes the xData for eval'''
        #[dates,recipients,forward,reply,numWords,top10,bottom10]
        dates = []
        recipients = []
        forward = []
        reply = []
        numWords = []
        #top10 = []
        #bottom10 = []
        tempTopBottom = [[1]*10]*20
        for doc in self.__evalDocs:
            dates.append(self.__dates[doc.getDate()])
            recipients.append(self.__names[doc.getToInfo()])
            forward.append(self.__forward[doc.getFwd()])
            reply.append(self.__reply[doc.getReply()])
            words = 0
            for s in range(doc.getSCount()):
                words += len(doc[s])
            numWords.append(words)
        self.__evalXData = [dates,recipients,forward,reply,numWords]
        self.__evalXData.extend(tempTopBottom)
    
    def train(self, xData, yData, maxDepth):
        '''makes the decision tree'''
        self.__tree = DecisionTreeClassifier(criterion="entropy",max_depth=maxDepth,random_state=0)
        self.__tree = self.__tree.fit(xData,yData)

    def eval(self, xData):
        return self.__tree.predict(self.__evalXData)

def testSKTree():
    """
    Used to test my SKTree
    """
    pass

if __name__ == "__main__":
    testSKTree()
