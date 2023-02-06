# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


my_list = [random.randint(0, 15) for el in range(random.randint(5, 10))]
sum_odd_positions = [el for i, el in enumerate(my_list, 1) if not i % 2]
print(f'В списке {my_list} на нечетных позициях находятся {sum_odd_positions} их сумма = {sum(sum_odd_positions)}')




