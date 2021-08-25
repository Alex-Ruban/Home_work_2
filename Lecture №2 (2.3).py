# 3.	Даны две квадратных таблицы чисел. Требуется построить третью, каждый элемент которой равен
# сумме элементов, стоящих на том же месте в 1-й и 2-й таблицах.
from random import randrange


def matrix_q(matrix_x, n):  # Функция вывода матриц
    for i in range(n):
        for j in range(n):
            print(str(matrix_x[i][j]).rjust(3), end=' ')
        print()


n = int(input('Укажите размерность квадратных матриц: '))
matrix_a = [[int(k) for k in [randrange(-99, 100) for _ in range(n)]] for _ in range(n)]
matrix_b = [[int(k) for k in [randrange(-99, 100) for _ in range(n)]] for _ in range(n)]

print('\nМатрица A: ')
matrix_q(matrix_a, n)

print('\nМатрица B: ')
matrix_q(matrix_b, n)

print('\nМатрица A + B:')
for i in range(n):
    for j in range(n):
        print(str(matrix_a[i][j] + matrix_b[i][j]).rjust(4), end=" ")
    print()
