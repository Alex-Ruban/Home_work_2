# Найдите сумму номеров минимального и максимального элементов.
# По целому n и n положительным целым числам определите, можно ли из них образовать подмножество, сумма элементов
# которого делится на n без остатка. Если можно, то найти любое из таких подмножеств.
from random import randrange

numbers = [randrange(-99, 100) for _ in range(int(input('Введите размерность списка: ')))]
print('Начальный список:', numbers)
print('Сумма  min и max  элементов: ', numbers.index(min(numbers)) + numbers.index(max(numbers)))

num_positive = list(filter(lambda x: x > 0, numbers))
print('Список положительных целых чисел', num_positive)

n = []
for i in range(len(num_positive)):
    for j in range(len(num_positive)):
        if i + j == len(num_positive):
            n.append((i, j))

print(f'Вариант подмножества: {n[0]}' if len(n) != 0 else 'Подмножеств нет.')
