# Напишите функцию, которая
# умножает матрицу на саму себя, но транспонированную
# берёт обратную матрицу от результата
import numpy as np

matrix1 = np.array([[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]])
matrix2 = np.array([[5, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]])
matrix3 = np.array([[9, -1], [1, 2], [2, 3], [3, 4], [4, 10]])


def print_vector(v):
    shape = v.shape

    if (len(shape) == 0):
        print(v)

    if (len(shape) == 1):
        s = ''
        for i in v:
            s += str(i) + '  '
        print(s)

    if (len(shape) == 2):
        for i in range(shape[0]):
            s = ''
            for j in range(shape[1]):
                s += str(v[i][j]) + '  '
            print(s)

def transpose_matrix(matrix):
    shape = matrix.shape

    out_matrix = np.zeros((shape[1], shape[0]))

    for i in range(shape[0]):
        for j in range(shape[1]):
            out_matrix[j, i] = matrix[i, j]

    return out_matrix

def prod_matrix(matrix1, matrix2):
    shape1 = matrix1.shape
    shape2 = matrix2.shape

    if (shape1[1] != shape2[0]):
        return np.array([])

    out_matrix = np.zeros((shape1[0], shape2[1]))

    for i in range(shape1[0]):
        for j in range(shape2[1]):
            curr_cell = 0
            for t in range(shape1[1]):
                curr_cell += matrix1[i, t] * matrix2[t, j]
                out_matrix[i, j] = curr_cell

    return out_matrix


def fun_fun(matrix):
    matrix_tr = transpose_matrix(matrix)
    matrix3 = prod_matrix(matrix, matrix_tr)
    matrix_inv = np.linalg.inv(matrix3)
    return matrix_inv

matrix_inv = fun_fun(matrix3)
print_vector(matrix_inv)
