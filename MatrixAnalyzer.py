from Debugger import *
import numpy as np

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
        # level_sets[i] = the level of i'th unknown
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

    '''
        -raw: returns the dictionary that has the format: {row_index, number of non-zero elements}
        -avg: returns average number of non-zeros per row
        -max: returns maximum number of non-zeros per row
        -std: returns standard deviation of non-zeros per row
    '''
    def get_nnz_per_row(self, csr_matrix, action="raw"):
        nnz_per_row = {}
        num_rows = csr_matrix.get_shape()[0]
        for row_id in range(0, num_rows):
            nnz_per_row[row_id] = csr_matrix.getrow(row_id).getnnz()
        if action == "avg":
            return np.array(list(nnz_per_row.values())).mean()
        if action == "max":
            return np.array(list(nnz_per_row.values())).max()
        if action == "std":
            return np.array(list(nnz_per_row.values())).std()
        if action == "raw":
            return nnz_per_row
        else:
            self.debugger.rise_Error("Unknown action for get_nnz_per_row: " + str(action))
            exit(1)

    '''
        -raw: returns the dictionary that has the format: {column_index, number of non-zero elements}
        -avg: returns average number of non-zeros per column
        -max: returns maximum number of non-zeros per column
        -std: returns standard deviation of non-zeros per column
    '''
    def get_nnz_per_column(self, csr_matrix,action="raw"):
        nnz_per_column = {}
        num_columns = csr_matrix.get_shape()[1]
        for column_id in range(0, num_columns):
            nnz_per_column[column_id] = csr_matrix.getcol(column_id).getnnz()
        if action == "avg":
            return np.array(list(nnz_per_column.values())).mean()
        if action == "max":
            return np.array(list(nnz_per_column.values())).max()
        if action == "std":
            return np.array(list(nnz_per_column.values())).std()
        if action == "raw":
            return nnz_per_column
        else:
            self.debugger.rise_Error("Unknown action for get_nnz_per_column: " + str(action))
            exit(1)