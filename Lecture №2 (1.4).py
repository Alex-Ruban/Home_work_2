# Найдите произведение элементов списка с нечетными номерами.
# Найдите наибольший элемент списка, затем удалите его и выведите новый список.
from random import randrange

numbers = [randrange(-99, 100) for _ in range(int(input('Введите размерность списка: ')))]
print('Начальный список:', numbers)

print('Произведение элементов списка с нечетными номерами:', sum([numbers[i] for i in range(1, len(numbers), 2)]))

numbers.remove(max(numbers))
print('Список без наибольшего элемента:', numbers)
