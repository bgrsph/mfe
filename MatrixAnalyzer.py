from Debugger import *
import numpy as np


class MatrixAnalyzer:
    def __init__(self, verbose):
        self.debugger = Debugger(verbose)

    def getLevels(self, csr_matrix):
        self.debugger.debug("Calculating Matrix Levels...")
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
                exit(1)
        self.debugger.debug("Matrix Levels Calculated")
        return level_sets

    def get_nnz_per_row(self, csr_matrix, action="raw"):
        """
        Parameters:
            csr_matrix (scipy.csr): the sparse matrix in CSR format
            action=avg (String): average number of non-zeros per row
            action=max (String): maximum number of non-zeros per row
            action=std (String): standard deviation of non-zeros per row
            action=raw (String): the dictionary that has the format: {row_index, number of non-zero elements}

        Returns:
            dictionary or float: statistics about number of non zeros elements in the columns of the matrix

        """
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

    def get_nnz_per_column(self, csr_matrix, action="raw"):
        """
         Parameters:
            csr_matrix (scipy.csr): the sparse matrix in CSR format
            action=avg (String): average number of non-zeros per column
            action=max (String): maximum number of non-zeros per column
            action=std (String): standard deviation of non-zeros per column
            action=raw (String): the dictionary that has the format: {column_index, number of non-zero elements}

         Returns:
            dictionary or float: statistics about number of non zeros elements in the columns of the matrix

         """
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

    def get_num_of_rows_per_level(self, level_set):
        rows_per_level = {n: [k for k in level_set.keys() if level_set[k] == n] for n in set(level_set.values())}
        num_rows_per_level = {}
        for level,rows in rows_per_level.items():
            num_rows_per_level[level] = len(rows)
        return num_rows_per_level