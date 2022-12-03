# print('1223')

# a = int(input('введите первое число :'))
# b = int(input('введите второе число :'))
# if a**2 == b:
#     print('первое число является квадратом второго')
# elif b**2 == a:
#     print('второе число является квадратом первого')
# else:
#     print('квадратов нет')

# a, b, c, d, e = int(input()), int(input()), int(
#     input()), int(input()), int(input())

# n = int(input('число:'))
# for i in range(-n, n+1):
#     print(i, end=',')
# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# num = input('введите 5 чисел через пробел :')
# num = num.split(' ')
# max = int(num[0])
# for i in num:
#     i = int(i)
#     if max < i:
#         max = i
# print(max)

# number = float(input('введите число: '))
# digit_first_float = int(number * 10) % 10
# if number == int(number):
#     print ('нет')
# else:
#     print(digit_first_float)
# 1) Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Пример*
# Ввод: 0,5
# Вывод: 5
# *Пример*
# Ввод: 3
# Вывод: Нет
# *Пример*
# Ввод: 0,04
# Вывод: 0

# 2) Напишите программу, в которой пользователь будет задавать две строки, одна из них - буква, а вторая фраза/слово,
# программа должна посчитать сколько раз буква встретилась буква во второй строке. (Не используя встроенные функции)

# a = float(input("введите дробное число: "))
# print(int(a * 10 % 10))

#  Петя и катя - брат и сестра. Петя - студент, а Катя - школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа, а Катя должна их отгадать
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P
# Помогите Кате отгадать задуманные Петей числа.

# *Пример*
# Ввод: 4 4
# Вывод: 2 2

# *Пример*
# Ввод: 5 6
# Вывод: 2 3

# n = int(input())

# suma = 0
# mult = 1

# while n > 0:
#     digit = n % 10
#     suma = suma + digit
#     mult = mult * digit
#     n = n // 10

# print("Сумма:", suma)
# print("Произведение:", mult)


# a = int(input("Введите сумму: "))
# b = int(input("Введите произведение: "))
# res = []
# for i in range(a + b):
#     if i == (a * i - b)**0.5:
#         res.append(i)
# print(*res if len(res) == 2 else res + res)


#  лекция 2

# colors = ["red", "green", "blue"]
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.write('tyr\n')
# data.close()
# exit()

# path ='file.txt'
# data =open(path,'r')
# for line in data:
#     print(line)
# data.close()

# def con(*par):
#     res: int = 0
#     for i in par:
#         res += i
#     return res


# print(con(1,3,6,7,8,6))


# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# ["Привет", "dfh4dfh", "12", "uran3"]
# 2 --- Da
# 1 --- Da
# 4 --- Da

# list1 =[input() for i in range(5)]
# num = input("введите число, которое будем искать в списке :")
# n = True
# for s in list1:
#     if num in s:
#         print('да')
#         n = False
#         break
# if n:
#     print('число не найдено')


# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# b = int(input('введите размерность списка: '))
# list1 =[input() for i in range(b)]
# num = input("введите строку, которую будем искать в списке: ")
# n = True
# coun = 0
# for i in range(b):
#     if num == list1[i]:
#         coun += 1
#     if coun == 2:
#         print(i)
#         n = False
#         break
# if n:
#     print(-1)


# 3. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

# import time
# print(time.time())
# print('введите границы для создания случайного числа')
# num1 = int(input('от: '))
# num2 = int(input('до: '))
# def get_rand():
#     return time.time.now().microsecond%10
# n = get_rand()
# print(int(len(str(num2))))
# print(n)

# day = int(input("Введите день недели  : "))
# if 0 < day < 8:
#     if day == 6 or day == 7:
#         print('выходной')
#     else:
#         print('будни')
# else:
#     print("введите другой день недели")

# day = int(input("Введите день недели  : "))
# match day:
#     case 1:
#         print('понедельник')
#     case 2:
#         print('вторник')
#     case 3:
#         print('среда')
#     case 4:
#         print('четверг')
#     case 5:
#         print('пятница')
#     case 6:
#         print('суббота')
#     case 7:
#         print('воскресенье')
#     case _:
#         print('не такого дня')

# coords = input('введите число: ').split(' ')

# print(coords)

# list = [2, 5, 4, 7]
# max = list[0]
# for i in range(len(list) - 1):
#     if list[i] > max:
#         max = list[i]

# print(max)
# a = 15
# c = 7.7
# x = '3.3'
# result = a + int(float(x)) + int(c)
# print(result)


# a = 15
# c = 7.7
# x = '3.3'
# result = a + int(float(x)) + int(c)
# print(result)

# name = "Ada Lovelace"
# print(name.upper())
# print(name.lower())
# print('1223 n\ 3445n\qwette34')
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[-1])


# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
  
#     1) с помощью математических формул нахождения корней квадратного уравнения
    
#     2) с помощью дополнительных библиотек Python
    
# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# Пример:
# Ввод:	3  5
# Вывод:	 15
# Ввод:	13 39
# Вывод:	  39
