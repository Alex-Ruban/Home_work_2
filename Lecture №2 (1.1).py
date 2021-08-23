# Удалить в списке все числа, которые повторяются более двух раз.
# Найти подмножество данного множества чисел такое, что сумма его элементов равна заданному числу.
from random import randrange

numbers = [randrange(-9, 10) for _ in range(int(input('Введите размерность списка: ')))]
print('Начальный список:', numbers)

for i in numbers:
    if numbers.count(i) > 1:
        numbers.remove(i)
print('Конечный список:', numbers)