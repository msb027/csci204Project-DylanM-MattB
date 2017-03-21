"""
Matt Brown
Dylan Mendelowitz
This file contains objects related to our plotting
"""


import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable


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
        '''
        wrapper for creating a 2D scatter plot
        '''
        x = xList
        y = yList
        plt.scatter(x,y)
        plt.xticks = xLabels
        plt.yticks = yLabels
        plt.show


    @staticmethod
    def twoDBar(xList, yList, xLabels=None, yLabels=None):
        '''
        wrapper to create a 2D bar graph
        '''
        n_groups = len(xList)
        index = np.arange(n_groups)
        bar_width = 0.1

        opacity = 0.8

        rects1 = plt.bar(index/2, max(yList) +10 , bar_width,\
                         alpha=opacity,\
                         color='g')
        plt.yticks(yLabels)
        plt.xticks(xLabels)
        plt.show





def testMyPlot():
    """
    Used to test MyPlot class
    """
    pass


if __name__ == "__main__":
    testMyPlot()


