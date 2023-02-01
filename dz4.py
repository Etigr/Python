from random import randint
import math


# 1 Вычислить число c заданной точностью d
# Пример:  при d = 0.001, π = 3.141   10^{-1} ≤ d ≤10^{-10}

# n = int(input('Введите количество знаков после запятой: '))
# print("значение PI", round(math.pi, n))

# через функцию

# def diskret(n):
#     count = 0 
#     while n % 1 != 0:
#         n *= 10
#         count += 1
#     return count

# n = float(input('Введите точность d = '))
# print(f'Pi  с заданой точностью = {round(math.pi, diskret(n))}')



# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def prostoydel(num):
   
#     x = 2
#     mnojetel = []
#     while x * x <= num:
#         while num % x == 0:
#             mnojetel.append(x)
#             num = num // x
#         x =x + 1
#     if x > 1:
#         mnojetel.append(num)
#     return mnojetel
# num = int(input('Введите натуральное число: '))
# print(prostoydel(num))
# ___________________________________________________________________


# def sieve_of_eratosthenes(number: int) -> list:
#     row = {i: '_' for i in range(2, number + 1) if i == 2 or i > 2 and i % 2 != 0}
#     # use a dict cause a list too expensive operation for deletion items
#     i = 2
#     while True:
#         if i ** 2 > number:
#             break
#         elif i != 2 and i % 2 == 0:
#             i += 1
#             continue

#         for j in range(i, number + 1, 2):
#             if j * i > number:
#                 break
#             elif (j * i) in row:
#                 del row[j * i]
#         i += 1
#     return list(row)


# def prime_factorization(number: int) -> list:
#     prime_numbers = sieve_of_eratosthenes(number)
#     if number in prime_numbers: return [number]
#     prime_factors = [i for i in prime_numbers if number % i == 0]
#     return prime_factors


# if __name__ == '__main__':
#     print(prime_factorization(2200))
#     print(prime_factorization(239))
#     print(prime_factorization(100))



# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

# def random_list(size: int, min_value = 0, max_value = 100):
#     new_list = []
#     for index in range(size + 1):
#         new_list.append(randint(min_value, max_value))
#     return new_list

# random_list = random_list(10, 0 , 10)
# print(random_list)

# new_list =[]

# for elem in random_list:
#     count = 0
#     for new_elem in random_list:
#         if elem == new_elem: 
#             count += 1
#     if count == 1: new_list.append(elem)

# print(new_list)
# _________________________________________________________

# def main():
#     user_array = []
#     result_array = []
#     user_array = list(map(int, input('Enter sequence of integer numbers. Use space bar to split. ').split()))

#     for element in user_array:
#         if user_array.count(element) == 1:
#             result_array.append(element)
#     print(f'Unique elements in array {user_array} are - ', end='')
#     print(result_array)


# if __name__ == "__main__":
#     main()
# ____________________________________________


# import random

# list_originals = []
# list_work = [1, 1, 0 , 2, 3, 4, 4, 5, 6 ]
# # for i in range(15):
# #     list_work.append(random.randint(0,7))

# #не совсем конкретное задание ...
# for i in list_work:
#     if i not in list_originals:
#         list_originals.append(i)
# print(list_work)
# #если нужно вывести только неповторяющиеся значения, т.е. без дубликатов        
# print(list_originals)

# #если нужно вывести только неповторяющиеся значения, т.е. исключить полностью те числа, что повторялись
# for i in list_originals:
#     if list_work.count(list_originals[i]) > 1:
#         while list_work.count(list_originals[i]) > 0:
#             list_work.pop(list_work.index(list_originals[i]))



# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
# *Пример:*  k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# def general_koef(n):

#     mnogochlen = ""
        
#     for i in range(n, -1, -1):
#         rnd = randint(0,10)
#         if rnd != 0:
#             if len(mnogochlen) > 1:
#                 mnogochlen += " + "
#             if i == 0:
#                 mnogochlen += str(rnd)
#             else:
#                 mnogochlen += str(rnd) + "*x^" + str(i)
#     mnogochlen += " = 0"
#     return mnogochlen

# def main():
   
#     polynom = general_koef(k)
#     print("Случайный многочлен:", polynom)
#     with open("dz4_5.txt", "w") as file1:
#         file1.write(polynom)

# k = int(input('Введите степень k: '))

# if __name__ == "__main__":
#     main()
# _______________________________________________

# import random
# from os import system

# system("cls")

# k = int(input('Enter degree of number: '))

# polynominal = ''
# for i in range(k, 0, -1):
#     polynominal += str(random.randrange(0,2)) + '*x^' + str(i) + ' + '
# polynominal += str(random.randrange(0,2)) + ' = 0'
# print(polynominal)

# with open('polynominal.txt', "w") as f_obj:
#     print(polynominal, file=f_obj, end='')


# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.


# def readFromFile(_file):

#     data = ""
#     with open(_file) as rfile:
#         data = rfile.read()
#     return data

# num_1 = readFromFile('dz4_4.txt')
# num_2 = readFromFile('dz4_5.txt')
# # print(num_1)
# # print(num_2)
# num_1 = num_1[:num_1.find('=')].split('+')
# num_2 = num_2[:num_2.find('=')].split('+')
# num_all = num_1 + num_2

# my_dict = {}

# for elem in num_all:
#     if 'x' not in elem:
#         key = 0
#     elif '^' not in elem:
#         key = 1
#     else:
#         key = int(elem[elem.find('^') + 1:])
        
#     if key > 0:
#         if key in my_dict:
#             my_dict[key] += int(elem[:elem.find('*')])
#         else:
#             my_dict[key] = int(elem[:elem.find('*')])
#     else:
#         if key in my_dict:
#             my_dict[0] += int(elem)
#         else:
#             my_dict[0] = int(elem) 
#     # print(my_dict)

# my_str = '' 
# for key, value in sorted(my_dict.items(),reverse=True):
#     if key == 0:
#         my_str += str(value)
#     elif key == 1:
#         my_str += f'{value}*x + '
#     else:
#         my_str += f'{value}*x^{key} + '
    
# my_str = my_str + ' = 0'
# # print(my_str)
# data = open('dz4_5sum.txt', 'w')
# data.write(my_str)




