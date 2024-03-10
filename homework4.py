import random

def generate_random_matrix(rows, cols):
    matrix =[]
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(1, 100))
        matrix.append(row)
    return matrix


def get_column_sum(matrix, col):
    sum = 0
    for row in matrix:
        sum += row[col]
    return sum
    

def get_row_average(matrix, row):
    sum = 0
    for elem in matrix[row]:
        sum += elem
    return sum/len(matrix[row])

matrix = generate_random_matrix(4,4)
print(matrix)

col_sum = get_column_sum(matrix, 2)
print(col_sum)


row_average = get_row_average(matrix, 2)
print(row_average)