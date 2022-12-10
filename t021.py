# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

my_list = [1, 2, 3, 4, 22, 234, 24]
x = [i for i in my_list if len(str(i)) == 2]            # List Comprehension
print(x)

x = []
for i in my_list:                                       # стандартно
    if len(str(i)) == 2:
        x.append(i)
print(x)

x = list(filter(lambda i: len(str(i)) == 2, my_list))   # filter
print(x)
