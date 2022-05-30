from math_and_stat import create_matrix, matrixDet
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = [
            [1, 2, 3, 5],
            [4, 5, 6, 3],
            [7, 8, 9, 3],
            [2, 1, 4, 2]]

k = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
b = create_matrix.reduce_matrix(True, k, 0, 0)
print(b)

abc = 1 