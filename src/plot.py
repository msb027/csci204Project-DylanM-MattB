"""
This file contains objects related to our plotting
"""


import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


class MyPlot:
    """
    This class will be used for all plotting.
    In most cases, the functions will just be static
    However, this allows for on nice interface
    """

    def __init__(self):
        """
        constructor
        """
        pass


    @staticmethod
    def twoDScatter(xList, yList, xLabels=None, yLabels=None):
        pass


    @staticmethod
    def twoDBar(xList, yList, xLabels=None, yLabels=None):
        pass





def testMyPlot():
    """
    Used to test MyPlot class
    """
    pass


if __name__ == "__main__":
    testMyPlot()


