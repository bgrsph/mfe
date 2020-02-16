from Debugger import *


class MatrixAnalyzer:
    def __init__(self, verbose):
        self.debugger = Debugger(verbose)

    def getLevels(self, csr_matrix):
        self.debugger.debug("Calculating Matrix Levels")
        level_sets = {}
        num_rows = csr_matrix.get_shape()[0]
        num_columns = csr_matrix.get_shape()[1]
        for i in range(0, num_rows):
            level_sets[i] = 0

        for i in range(0, num_rows):
            local_max = float('-inf')
            for j in range(0, num_columns):
                if csr_matrix[i, j] != 0:
                    if level_sets[j] > local_max:
                        local_max = level_sets[j]
            level_sets[i] = 1 + local_max

            # It means matrix either cannot be read or it's empty somehow
            if local_max == float('-inf'):
                self.debugger.rise_Error("Rows or Columns cannot be read during Level Calculation")
        return level_sets

