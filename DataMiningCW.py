import numpy as np
deep, matrix_range = [int(i) for i in input().split()]
mat_in = np.array([list(map(int,input().split())) for i in range(matrix_range)], list)
mat_out = np.transpose(mat_in)
h = np.ones((matrix_range,1))
a = []
for i in range(deep):
    mat = np.dot(mat_out, h)
    a = mat/mat.max()
    mat = np.dot(mat_in, a)
    h = mat/mat.max()
print("Метрика A:")
print(a)
print("Метрика H:")
print(h)


