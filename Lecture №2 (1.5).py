# Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.
from random import randrange

numbers = [randrange(-10, 10) for _ in range(int(input('Введите размерность списка: ')))]
print('Начальный список:', numbers)

numbers_min = [i for i in numbers if i % 2 == 0]
print(f'Минимальный элемент: {min(numbers_min)}' if len(numbers_min) > 0 else f'Первый элемент: {numbers[0]}')

# Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные
if numbers.count(0) > 0:
    numbers_new = []
    for j in range(numbers.count(0)):
        numbers.remove(0)
        numbers_new.append(0)
    print('Преобразованный список: ', numbers_new + numbers)
else:
    print('Нулей в списке нет')