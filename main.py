from MatrixDownloader import MatrixDownloader
from MatrixAnalyzer import *
import numpy as np
# Make the verbose True to see the progress
verbose = False

# Initializing classes
matrix_downloader = MatrixDownloader(verbose=verbose)
matrix_analyzer = MatrixAnalyzer(verbose=verbose)

CSR_Matrix_Lower_Triangular = matrix_downloader.getCSRMatrix(matrix_id=232, diagonal="lower")
#level_sets = matrix_analyzer.getLevels(csr_matrix=CSR_Matrix_Lower_Triangular)
#nnz_per_row = matrix_analyzer.get_nnz_per_row(csr_matrix=CSR_Matrix_Lower_Triangular,action="raw")
#avg_nnz_per_row = matrix_analyzer.get_nnz_per_row(csr_matrix=CSR_Matrix_Lower_Triangular,action="avg")
#std_nnz_per_row = matrix_analyzer.get_nnz_per_row(csr_matrix=CSR_Matrix_Lower_Triangular,action="std")
#nnz_per_column = matrix_analyzer.get_nnz_per_column(csr_matrix=CSR_Matrix_Lower_Triangular,action="raw")
#avg_nnz_per_column = matrix_analyzer.get_nnz_per_column(csr_matrix=CSR_Matrix_Lower_Triangular,action="avg")
#std_nnz_per_column = matrix_analyzer.get_nnz_per_column(csr_matrix=CSR_Matrix_Lower_Triangular,action="std")
