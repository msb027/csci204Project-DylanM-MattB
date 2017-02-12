"""
Main Interface 
Requirements:  matplotlib, numpy, scipy, sci-kit
Recommended to use with anaconda (will have all packages)
"""

from util import *


def main():
    """
    Will call main loop of interface
    """
    user_interface()

def user_interface():
    """
    Will be used to interact with user
    """

    info = UserInput() #my main structure that holds my execution information

    print("----Welcome to Enron Data Analysis----")
    print("Goals: (1) Who wrote an email (2) Communication Network -- Who talked to who")
    tpath = input("Please enter the filepath for the training data: ")
    info.tpath = tpath
    print("Loading Training Documents")
    #FILL ME WITH CODE TO DO THIS, WRITE OUT IF SUCCESSFUL
    epath = input("Please enter the filepath for the unknown data: " )
    info.epath = epath
    print("Loading Eval Documents")
    #FILL ME WITH CODE TO DO THIS, WRITE OUT IF SUCCESSFULL

    
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
    t = int(input("?"))
    
    #FILL ME, test if t is ok, if not do something smart

def addTextFilter(info):
    """
    Add information about which text filters to use, see TextFilter class for details
    """
    print("Student to add")
    return None

def applyTextFilter(info):
    """
    Apply the text filter to both the training and eval Document Lists
    """
    print("Student to add")
    return None

def topicAnalyisTrain(info):
    """
    We will analyze topics based on words in the email
    We will prompt the user for how many topics "words" they are looking for
    After we will find this information and plot it using our Plot class
    """
    print("Student to add")
    return None


def topicAnalysisEval(info):
    """
    We will analyze topics based on words in the email
    We will prompt the user for how many topics "words" they are looking for
    After we will find this information and plot it using our Plot class
    """
    print("Student to add")
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


if __name__ == "__main__":
    main()
