# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# num = [2, 3, 4, 5, 6]
# num1 = []
# while len(num) > 0:
#     if len(num) == 1:
#         num1.append(num.pop()**2)
#     else:
#         num1.append(num.pop(0)*num.pop())
#     # print(num)
# print(f'ответ :  {num1}')

import random
def sumofen(mass):
    resmass=[]
    for i in range(len(mass)//2):
        resmass. append(mass[i]*mass[len(mass)-1-i])
        print(resmass)
a = [random.randint(1, 5)for i in range(6)]
print(a)
print(sumofen(a))

# непонятно что