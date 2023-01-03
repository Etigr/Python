# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


# num = (input('Введите вещественное число: '))
# sum = 0
# for i in num:
#     if i != '.' and i != ',' and i != '-':
#         sum += int(i)
# print(sum)

# abs -не работает с большими числами((



# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input('Введите число N: '))
# sum = 1
# for i in range(num):
#     sum *= i + 1
#     print(sum, end= ' ')



# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# num = int(input('Введите число n: '))
# sum = 0
# my_dict = {}
# for i in range(1, num+1):
#     my_dict[i] = round((1+1/i)**i, 2)
#     sum += my_dict[i]
# print(f'Для n={num}:  {my_dict}, сумма = {sum}') 



# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# import random

# num = int(input("Введите число: "))  
# my_list = []
# for i in range(num):
#     my_list.append(random.randint(1, num))
# print(my_list)

# data = open('file.txt', 'r')
# mult = 1
# for line in data:
#     mult *= my_list[int(line)]
#     # print(line, end='')
    
# print(f'Произведение элементов указаных в файле равна {mult}')



# 5. Реализуйте алгоритм перемешивания списка.

# import random

# N = int(input("Введите длину списка: "))
# num = list(range(N))
# print(num)
# for i in range(len(num)):
#     num.insert(random.randint(0, len(num)-1), num.pop(i))
# print(num)