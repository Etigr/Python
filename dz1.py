# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.

# num = int(input('Введите порядковый номер дня недели от 1 до 7: '))
# if num in (6,7):
#     if num == 6:
#         print("Сегодня cуббота")
#     if num == 7:
#         print("Сегодня воскресенье")
#     print("Можно отдохнтуть :)")
# elif num in (1,2,3,4,5):
#     print("Иди работай :(")
#     if num == 1:
#         print("Сегодня понедельник")
#     if num == 2:
#         print("Сегодня вторник")
#     if num == 3:
#         print("Сегодня среда")
#     if num == 4:
#         print("Сегодня четверг")
#     if num == 5:
#         print("Сегодня пятница")
# else:
    # print("Ошибка ввода")   


# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех 
# значений предикат.

# for x in [1, 0]:
#     for y in [1, 0]:
#         for z in [1, 0]:
#             print(x,y,z, end=' -> ')
#             if not (x and y and z) == (not x) or (not y) or (not z):
#                 print("Истина")
#             else:             
#                 print("Ложь")
            


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт 
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# print("Чтобы узнать четверть, введите точку с координатами Х, Y (X ≠ 0 и Y ≠ 0)")
# x, y = float(input('Введите Х:')), float(input('Введите Y:'))
# if x > 0 and y >0:
#     print("I четверть")
# elif x < 0 and y >0:
#     print("II четверть")
# elif x < 0 and y < 0:
#     print("III четверть")
# elif x > 0 and y < 0:
#     print("IV четверть")
# elif x == 0 and y > 0:
#     print("Точка лежит на оси ординат между I и II четвертями")
# elif x == 0 and y < 0:
#     print("Точка лежит на оси ординат между III и IV четвертями")
# elif x > 0 and y == 0:
#     print("Точка лежит на оси абцисс между I и IV четвертями")
# elif x < 0 and y == 0:
#     print("Точка лежит на оси абцисс между II и III четвертями")
# else:
#     print("Ошибка, это начало координат")

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек 
# в этой четверти (x и y).

# chetvert = int(input('Введите одну из 4-х четвертей, чтобы узнать диапазон : '))
# my_dict = {1: 'x > 0 and y >0', 2: 'x < 0 and y >0', 3: 'x < 0 and y < 0', 4: 'x > 0 and y < 0'}
# if chetvert == 1:
#     print(my_dict.get(1))
# elif chetvert == 2:
#     print(my_dict.get(2))
# elif chetvert == 3:
#     print(my_dict.get(3))
# elif chetvert == 4:
#     print(my_dict.get(4))
# else:
#     print("Такой четверти нет")


# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними 
# в 2D пространстве.

# print("Введите 1 точку с координатами Х1, Y1")
# x1, y1 = int(input('Введите Х1: ')),int(input('Введите Y1: '))
# print("Введите 2 точку с координатами Х2, Y2")
# x2, y2 = int(input('Введите Х2: ')),int(input('Введите Y2: '))
# print(round(float(((x1 - x2)**2 + (y1-y2)**2)**0.5), 2))