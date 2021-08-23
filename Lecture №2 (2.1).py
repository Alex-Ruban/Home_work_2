# В матрице найти номер строки, сумма чисел в которой максимальна.
from random import *

print('Укажите размерность матрицы.')
print("Число строк:", end=' ')
n = int(input())
print("Число столбцов:", end=' ')
m = int(input())
matrix = [[int(k) for k in [randrange(-9, 10) for _ in range(m)]] for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).rjust(2), end=' ')
    print()

max_sum = []
for i in matrix:
    max_sum.append(sum(i))
print('Номер строки, сумма чисел в которой максимальна:', max_sum.index(max(max_sum)))
