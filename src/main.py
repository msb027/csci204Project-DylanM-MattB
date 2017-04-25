"""
Names: Dylan Mendelowitz and Matt Brown
Main Interface 
Requirements:  matplotlib, numpy, scipy, sci-kit
Recommended to use with anaconda (will have all packages)
"""

from util import *
import os
from documentReader import DocumentReader
from stats import Stats
from plot import MyPlot
from textFilter import *

global filterList

def main():
    """
    Will call main loop of interface
    """
    user_interface()

def listDir(path, docList):
    if not os.path.isdir( path ):
        print( path )
    else:
        # Print the contents in this directory
        # List everything
        
        for f in os.listdir( path ):
            v = os.path.joint(path,f)
            reader = DocumentReader(v)
            docs.append(reader.readFile)
        for f in os.listdir( path ):
            # Convert it into a complete path, needed for 'isdir()'
            # 'v' will be needed to run 'isdir()' when recursive call is made
            v = os.path.join( path, f )
            aPath = os.path.abspath(v)
            if os.path.isdir(aPath):
                listDir(aPath, docList)
                
def user_interface():
    """
    Will be used to interact with user
    """

    info = UserInput() #my main structure that holds my execution information

    print("----Welcome to Enron Data Analysis----")
    print("Goals: (1) Who wrote an email (2) Communication Network -- Who talked to who")
    tpath = input("Please enter the filepath for the training data: ")
    info.tPath = tpath
    print("Loading Training Documents")
    #FILL ME WITH CODE TO DO THIS, WRITE OUT IF SUCCESSFUL
    docs = []
    listDir(tpath, docs)
    info.setTDocument(docs)
    print('Training Files added successfully')
    epath = input("Please enter the filepath for the unknown data: " )
    info.ePath = epath
    print("Loading Eval Documents")
    #FILL ME WITH CODE TO DO THIS, WRITE OUT IF SUCCESSFULL
    docs = []
    listDir(epath, docs)
    info.setEDocument(docs)
    print('Eval Files added successfully')

    
    #FILL ME... if everything is ok call the topMenu
    topMenu(info)
      

def topMenu(info):
    
    print("Enter Selection")
    print("1. Add Text Filter")
    print("2. Apply Text Filter")
    print("3. Topic Analyis of Train")
    print("4. Topic Analyis of Eval")
    print("5. Find UnKnown From")
    print("6. Find UnKnown To")
    print("7. Build Social Network Graph")
    print('8. Build skTree')
    print('9. Build our Decision Tree')
    t = int(input("?"))
    
    if t < 1 or t > 7:
        print('Please enter a number from 1 to 7')
        topMenu(info)
    elif t == 1:
        print('adding text filter')
        addTextFilter(info)
    elif t == 2:
        print('applying text filter')
        applyTextFilter(info)
    elif t == 3:
        print('starting topic analysis of train')
        topicAnalysisTrain(info)
    elif t == 4:
        print('starting topic analysis of eval')
        topicAnalysisEval(info)
    elif t == 5:
        print('Finding uknown from')
        findUnKnownFrom(info)
    elif t == 6:
        print('Finding uknown to')
        findUnKnownTo(info)
    elif t ==7:
        print('Building social network')
        buildNetwork(info)
    elif t == 8:
        predictSKTree(info)
    else:
        predictmyTree(info)

def addTextFilter(info):
    """
    Add information about which text filters to use, see TextFilter class for details
    """
    filterList = []
    print("Please select the text filters you would like to add. Hit Return after each number you add, enter 6 when you have added all of the "\
          "filters you would like:")
    while True:
        print("Enter Selection")
        print("1. normalize white space")
        print("2. normalize case")
        print("3. strip null")
        print("4. strip numbers")
        print("5. strip files")
        print("6. End")
        t = int(input("?"))
        
        if t < 1 or t > 6:
            print('Please enter a number from 1 to 6')
            addTextFilter(info)
        elif t == 1:
            filterList.append('normalizeWhiteSpace')
        elif t == 2:
            filterList.append('normalizeCase')
        elif t == 3:
            filterList.append('stripNull')
        elif t == 4:
            filterList.append('stripNumbers')
        elif t == 5:
            filterList.append('stripFiles')
        else:
            info.setTextFilter(filterList)
            break
    

def applyTextFilter(info):
    """
    Apply the text filter to both the training and eval Document Lists
    """
    filterInstance = TextFilter(info.getTextFilter())
    tempTDoc = info.getTDocument()
    tempEDoc = info.getEDocument()
    
    for doc in tempTDoc:
        filterInstance.apply(doc)
    
    for doc in tempEDoc:
        filterInstance.apply(doc)
        
    print('Text filters applied successfully!')

def topicAnalysisTrain(info):
    """
    We will analyze topics based on words in the email
    We will prompt the user for how many topics "words" they are looking for
    After we will find this information and plot it using our Plot class
    """
    try:
        numTopics = int(input('How many topics(words) are you looking for?'))
    except:
        print('Please make sure your input in a number')
        topicAnalysisTrain(info)
        
    wordList = []
    for document in info.getTDocument():
        for i in range(document.getSCount()):
            wordList.extend(document[i].split())
    
    freqDic = Stats.findFreqDic(wordList)
    topN = Stats.topNSort(freqDic,numTopics)
    bottomN = Stats.bottomNSort(freqDic,numTopics)

    MyPlot.twoDBar(list(topN),topN.values, list(topN), topN.values)
    MyPlot.twoDBar(list(bottomN), bottomN.values, list(bottomN), bottomN.values)
    return None
    


def topicAnalysisEval(info):
    """
    We will analyze topics based on words in the email
    We will prompt the user for how many topics "words" they are looking for
    After we will find this information and plot it using our Plot class
    """
    try:
        numTopics = int(input('How many topics(words) are you looking for?'))
    except:
        print('Please make sure your input in a number')
        topicAnalysisEval(info)
        
    wordList = []
    for document in info.getEDocument():
        for i in range(document.getSCount()):
            wordList.extend(document[i].split())
    
    freqDic = Stats.findFreqDic(wordList)
    topN = Stats.topNSort(freqDic,numTopics)
    bottomN = Stats.bottomNSort(freqDic,numTopics)

    MyPlot.twoDBar(list(topN),topN.values, list(topN), topN.values)
    MyPlot.twoDBar(list(bottomN), bottomN.values, list(bottomN), bottomN.values)
    return None

def findUnKnownFrom(info):
    """
    To be added (decision tree, pca, seq)
    """
    print("To be added")
    return None

def findUnKnownTo(info):
    """
    To be added (decision tree, pca, seq)
    """
    print("To be added")
    return None


def buildNetwork(info):
    """
    To be added (may or maynot get)
    """
    print("To be added")
    return None

def predictSKTree(info):
    skTree = SKTree(info.getTDocument, info.getEDocument)
    result = skTree.getPrediction()
    return result

def predictmyTree(info):
    myTree = myDecisionTree(info.getTDocument(),info.getEDocument)
    return myTree
    

if __name__ == "__main__":
    main()
