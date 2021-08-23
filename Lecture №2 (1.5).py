# Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.
# Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные
from random import randrange

numbers = [randrange(-99, 100) for _ in range(int(input('Введите размерность списка: ')))]
print('Начальный список:', numbers)

numbers_min = [i for i in numbers if i % 2 == 0]
print(f'Минимальный элемент: {min(numbers_min)}' if len(numbers_min) > 0 else f'Первый элемент: {numbers[0]}')

