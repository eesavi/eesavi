import numpy as np
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

matrix1 = np.array([[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]])
matrix2 = np.array([[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]])
matrix3 = np.array([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]])
print(matrix1.shape)
print_vector(matrix1)
print()
print(matrix2.shape)
print_vector(matrix2)
print()
print(matrix3.shape)
print_vector(matrix3)


def prod_matrix(matrix1, matrix2, matrix3):
    shape1 = matrix1.shape
    shape2 = matrix2.shape
    shape3 = matrix3.shape

    if (shape1[1] != shape2[0]) or (shape2[1] != shape3[0]):
        return np.array([])
    else:
        out_matrix = np.zeros((shape1[0], shape2[1]))

        for i in range(shape1[0]):
            for j in range(shape2[1]):
                curr_cell = 0
                for t in range(shape1[1]):
                    curr_cell += matrix1[i, t] * matrix2[t, j]
                    out_matrix[i, j] = curr_cell

        out_matrix2 = np.zeros((shape1[0], shape3[1]))

        for i in range(shape1[0]):
          for j in range(shape3[1]):
            curr_cell = 0
            for t in range(shape2[1]):
                curr_cell += out_matrix[i, t] * matrix3[t, j]
                out_matrix2[i, j] = curr_cell
    #return out_matrix
    return out_matrix2

print()
out_matrix2 = prod_matrix(matrix1, matrix2, matrix3)
print_vector(out_matrix2)
