# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# num = [2, 3, 5, 9, 3]
# summ = 0
# for i in range(1, len(num), 2):
#     summ += num[i]
# print(f'{num}  сумма элементов списка, стоящих на нечётной позиции: {summ}')

# a = input(' введите число через пробел: ').split()
# i = 1
# while (i < len(a)//2+len(a) % 2):
#     num = len(a) - i-1
#     print(int(a[i])*int(a[num]), end=" ")
#     i+=1


import random
def sumofen(mass):
    count = 0
    for i in range(1, len(mass), 2):
        count += mass[i]
    print(count)
a = [random.randint(1, 5)for i in range(6)]
print(a)
sumofen(a)
