import numpy as np

deep, matrix_range = [int(i) for i in input().split()]
# deep - количество итераций, "глубина" поиска. matrix_range - количество вершин в графе
mat_in = np.array([list(map(int,input().split())) for i in range(matrix_range)], list)
# вводим матрицу, описывающую граф
mat_out = np.transpose(mat_in)
# Получаем транспонированную матрицу
h = np.ones((matrix_range,1))
a = []
for i in range(deep):
    mat = np.dot(mat_out, h)
    a = mat/mat.max()
    mat = np.dot(mat_in, a)
    h = mat/mat.max()
# Применяем HITS, выводим значения метрик
print("Метрика A:")
print(a)
print("Метрика H:")
print(h)


