import random

class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def mean(self):
        total_sum = sum(sum(row) for row in self.matrix)
        return total_sum / (self.rows * self.cols)

    def sum_row(self, row_num):
        if row_num < 0 or row_num >= self.rows:
            return "Invalid row number"
        return sum(self.matrix[row_num])

    def average_column(self, col_num):
        if col_num < 0 or col_num >= self.cols:
            return "Invalid column number"
        total = sum(row[col_num] for row in self.matrix)
        return total / self.rows

    def print_submatrix(self, col1, col2, row1, row2):
        if col1 < 0 or col2 >= self.cols or row1 < 0 or row2 >= self.rows:
            return "Invalid submatrix coordinates"
        for i in range(row1, row2 + 1):
            print(self.matrix[i][col1:col2 + 1])



matrix = Matrix(3, 3)
print("Generated Matrix:")
matrix.print_matrix()
print("Mean of the matrix:", matrix.mean())
print("Sum of row 1:", matrix.sum_row(1))
print("Average of column 2:", matrix.average_column(2))
print("Submatrix:")
matrix.print_submatrix(0, 1, 1, 2)