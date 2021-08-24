# Симметричная матрица.
# Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.
from random import *

n = int(input('Укажите размерность квадратной матрицы: '))
matrix = [[int(k) for k in [randrange(1, 3) for _ in range(n)]] for _ in range(n)]

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()

flag = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False

print('ДА! матрица симметрична.' if flag else 'Матрица несимметрична')