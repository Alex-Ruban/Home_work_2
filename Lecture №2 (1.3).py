# Найдите сумму отрицательных элементов списка.
# Найдите сумму элементов списка между двумя первыми нулями. Если двух нулей нет в списке, то выведите ноль.
from random import randrange

numbers = [randrange(-9, 10) for _ in range(int(input('Введите размерность списка: ')))]
print('Начальный список:', numbers)

print('Сумма отрицательных элементов:', sum([i for i in numbers if i < 0]))

if numbers.count(0) > 1:
    item = [j for j in range(len(numbers)) if numbers[j] == 0]
    print('Сумма элементов списка между двумя первыми нулями:', sum(numbers[item[0]:item[1]]))
else:
    print('Двух нулей нет:', 0)
