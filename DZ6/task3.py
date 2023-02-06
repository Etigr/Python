#  Напишите программу на Python для поиска пересечения двух заданных массивов 
# с помощью Lambda, filter.



a = [1, 2, 3, 5, 7, 8, 9, 10]
b = [1, 2, 4, 8, 9]
res = list(filter(lambda x: x in a, b))
res1 = list(filter(lambda x: x in b, a))
print(res)
print(res1)