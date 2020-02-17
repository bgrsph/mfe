from MatrixDownloader import *
from MatrixAnalyzer import *
from Plotter import *
from FileManager import *

MATRIX_ID = 2

# Make it True to see the progress
verbose = True

# Initialize classes
matrix_downloader = MatrixDownloader(verbose=verbose)
matrix_analyzer = MatrixAnalyzer(verbose=verbose)
plotter = Plotter(verbose=verbose)
fileManager = FileManager(verbose=verbose)

# Create files for results
fileManager.createDirForResults(path="results")
fileManager.createDirForMatrix(matrixID=MATRIX_ID)


# Download the matrix
CSR_Matrix_Lower_Triangular = matrix_downloader.getCSRMatrix(matrix_id=MATRIX_ID, diagonal="lower")

# Extract the features
level_sets = matrix_analyzer.getLevels(csr_matrix=CSR_Matrix_Lower_Triangular)
#nnz_per_row = matrix_analyzer.get_nnz_per_row(csr_matrix=CSR_Matrix_Lower_Triangular,action="raw")
#avg_nnz_per_row = matrix_analyzer.get_nnz_per_row(csr_matrix=CSR_Matrix_Lower_Triangular,action="avg")
#std_nnz_per_row = matrix_analyzer.get_nnz_per_row(csr_matrix=CSR_Matrix_Lower_Triangular,action="std")
#nnz_per_column = matrix_analyzer.get_nnz_per_column(csr_matrix=CSR_Matrix_Lower_Triangular,action="raw")
#avg_nnz_per_column = matrix_analyzer.get_nnz_per_column(csr_matrix=CSR_Matrix_Lower_Triangular,action="avg")
#std_nnz_per_column = matrix_analyzer.get_nnz_per_column(csr_matrix=CSR_Matrix_Lower_Triangular,action="std")
num_rows_per_level = matrix_analyzer.get_num_of_rows_per_level(level_set=level_sets)

plotter.plot_num_rows_per_level(matrix_ID=MATRIX_ID, dict=num_rows_per_level,cumulative=True)


























# TODO 1: histogram of normal nnz per level
# TODO 2: histogram of cumulative nnz per level

# TODO 3: histogram of normal number of rows/columns per level
# TODO 4: histogram of cumulative number of rows/columns per level

# TODO 5: histogram of running normal mean of nnz per row/column
# TODO 6: histogram of running harmonic mean of nnz per row/column

# TODO 7: folder name is ID, save all plots in that folder, each has one page.
# TODO 8: matrixID will be command line parameter

# Running avg nnz per row: 1+0/1 2+1/2, 3+2+1/3... nnz per row dictine bak

