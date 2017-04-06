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
        self.__words = {}
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
    
    def readDocs(self):
        nameCount = 0
        wordNumber = 0
        dateCount = 0
        for doc in self.__trainDocs:
            
            if doc.getToInfo() not in self.__names:
                self.__names[doc.getToInfo()] = nameCount
                nameCount += 1
            if doc.getFromInfo() not in self.__names:
                self.__names[doc.getFromInfo()] = nameCount
                nameCount += 1
                
            words = []
            for s in range(doc.getSCount()):
                words.extend(doc[s].split())
            freqDic = Stats.findFreqDic(words)
            top10 = Stats.topNSort(freqDic,10)
            bottom10 = Stats.bottomNSort(freqDic,10)
            for word in top10:
                if word not in self.__words:
                    self.__words[word] = wordNumber
                    wordNumber += 1
            for word in bottom10:
                if word not in self.__words:
                    self.__words[word] = wordNumber
                    wordNumber += 1
            
            if doc.getDate() not in self.__dates:
                self.__dates[doc.getDate()] = dateCount
                dateCount += 1
                
        for doc in self.__evalDocs:
            if doc.getToInfo() not in self.__names:
                self.__names[doc.getToInfo()] = nameCount
                nameCount += 1
    
    def createXData(self):
        #[dates,recipients,forward,reply,numWords,top10,bottom10]
        dates = []
        recipients = []
        forward = []
        reply = []
        numWords = []
        #top10 = []
        #bottom10 = []
        tempTopBottom = [[1]*10]*20
        for doc in self.__trainDocs:
            dates.append(self.__dates[doc.getDate()])
            recipients.append(self.__names[doc.getToInfo()])
            forward.append(self.__forward[doc.getFwd()])
            reply.append(self.__reply[doc.getReply()])
            words = 0
            for s in range(doc.getSCount()):
                words += len(doc[s])
            numWords.append(words)
        self.__xData = [dates,recipients,forward,reply,numWords]
        self.__xData.extend(tempTopBottom)
    
    def createYData(self):
        for doc in self.__trainDocs:
            self.__yData.append(self.__names[doc.getFromInfo()])
    
    def createEvalXData(self):
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
