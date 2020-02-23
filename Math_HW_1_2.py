# Напишите функцию, которая считает разницу между максимальным и минимальным элементами матрицы
import numpy as np

matrix1 = np.array([[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]])
matrix2 = np.array([[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]])
matrix3 = np.array([[0, -1], [1, 2], [2, 3], [3, 4], [4, 10]])


def delta(matrix):
    shape = matrix.shape
    matrix_max = matrix[0, 0]
    matrix_min = matrix[0, 0]
    for i in range(shape[0]):
        for j in range(shape[1]):
            if matrix_max <= matrix[i, j]:
                matrix_max = matrix[i, j]
            if matrix_min >= matrix[i, j]:
                matrix_min = matrix[i, j]
    d = matrix_max - matrix_min
    return d

d = delta(matrix3)
print(d)