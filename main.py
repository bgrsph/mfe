from MatrixDownloader import MatrixDownloader
from MatrixAnalyzer import *

matrix_downloader = MatrixDownloader(verbose=True)
matrix_analyzer = MatrixAnalyzer(verbose=True)

CSR_Matrix_Lower_Triangular = matrix_downloader.getCSRMatrix(matrix_id=232, diagonal="lower")
level_sets = matrix_analyzer.getLevels(csr_matrix=CSR_Matrix_Lower_Triangular)

print(level_sets)

