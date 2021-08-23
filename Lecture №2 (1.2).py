# Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.
from random import randrange

numbers = [randrange(-9, 10) for _ in range(int(input('Введите размерность списка: ')))]
print('Начальный список:', numbers)

print('Наибольший нечетный элемент:', max([i for i in numbers if i % 2 != 0]))
print('Минимальный по модулю элемент списка:', min([abs(i) for i in numbers]))
