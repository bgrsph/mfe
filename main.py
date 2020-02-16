from MatrixDownloader import *
from MatrixAnalyzer import *

# Make it True to see the progress
verbose = False

# Initialize classes
matrix_downloader = MatrixDownloader(verbose=verbose)
matrix_analyzer = MatrixAnalyzer(verbose=verbose)

# Download the matrix
# TODO: Najeeb may want other matrix formats like COO, if so add a parameter to getMatrix() function
CSR_Matrix_Lower_Triangular = matrix_downloader.getCSRMatrix(matrix_id=232, diagonal="lower")

# Extract the features
level_sets = matrix_analyzer.getLevels(csr_matrix=CSR_Matrix_Lower_Triangular)
#nnz_per_row = matrix_analyzer.get_nnz_per_row(csr_matrix=CSR_Matrix_Lower_Triangular,action="raw")
#avg_nnz_per_row = matrix_analyzer.get_nnz_per_row(csr_matrix=CSR_Matrix_Lower_Triangular,action="avg")
#std_nnz_per_row = matrix_analyzer.get_nnz_per_row(csr_matrix=CSR_Matrix_Lower_Triangular,action="std")
#nnz_per_column = matrix_analyzer.get_nnz_per_column(csr_matrix=CSR_Matrix_Lower_Triangular,action="raw")
#avg_nnz_per_column = matrix_analyzer.get_nnz_per_column(csr_matrix=CSR_Matrix_Lower_Triangular,action="avg")
#std_nnz_per_column = matrix_analyzer.get_nnz_per_column(csr_matrix=CSR_Matrix_Lower_Triangular,action="std")

#rowID_per_level = matrix_analyzer.get_rowID_per_level(csr_matrix=CSR_Matrix_Lower_Triangular)

print(level_sets)
# TODO: Plot all the features and graphs in a single page
# TODO: Ask Najeeb how he wants to organize the files so that the program saves them accordingly