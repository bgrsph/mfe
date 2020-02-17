import matplotlib.pyplot as plt
from Debugger import *
from FileManager import *


class Plotter:
    def __init__(self,verbose):
        self.debugger = Debugger(verbose=verbose)
        self.fileManager = FileManager(verbose=verbose)

    def plot_num_rows_per_level(self, matrix_ID, dict, cumulative):
        self.debugger.debug("Plotting Number of Rows per Level for Matrix ID: " + str(matrix_ID))
        plt.hist(list(dict.keys()), weights=list(dict.values()),
                 bins=len(dict.values()), cumulative=cumulative)
        plt.title("Number of Rows per Level")
        plt.xlabel("Levels")
        plt.ylabel("Number of Rows")
        plt.savefig(self.fileManager.getMatrixFilePath(matrix_ID) + "/num_rows_per_level")
        plt.show()