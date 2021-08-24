# В матрице найти номер строки, сумма чисел в которой максимальна.
from random import *

print('Параметры матрицы:')
n = int(input("Число столбцов: "))
m = int(input("Число строк: "))
matrix = [[int(k) for k in [randrange(-9, 10) for _ in range(n)]] for _ in range(m)]
print()
for i in range(m):
    for j in range(n):
        print(str(matrix[i][j]).rjust(2), end=' ')
    print()

max_sum = [sum(k) for k in matrix]
print('\nНомер строки, сумма чисел в которой максимальна:', max_sum.index(max(max_sum)) + 1)
