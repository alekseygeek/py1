# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 24
# 2 2 2 3

x = int(input("Введите натуральное число :  "))
y = []
n = x
if n%2 == 0:
    while x%2 == 0:
        x = x/2 
        y.append(x)
    print(y) 



















# n = 24

# # список заполняется значениями от 0 до n
# a = []
# for i in range(n + 1):
#     a.append(i)
# # Вторым элементом является единица,
# # которую не считают простым числом
# # забиваем ее нулем.
# a[1] = 0
# # начинаем с 3-го элемента
# i = 2
# while i <= n:
#     # Если значение ячейки до этого
#     # не было обнулено,
#     # в этой ячейке содержится
#     # простое число.
#     if a[i] != 0:
#         # первое кратное ему
#         # будет в два раза больше
#         j = i + i
#         while j <= n:
#             # это число составное,
#             # поэтому заменяем его нулем
#             a[j] = 0
#             # переходим к следующему числу,
#             # которое кратно i
#             # (оно на i больше)
#             j = j + i
#     i += 1
# # Превращая список во множество,
# # избавляемся от всех нулей кроме одного.
# a = set(a)
# # удаляем ноль
# a.remove(0)
# print(a)

# answer = []
# for num in a:
#     if not (n % num):
#         answer.append(num)
# print(answer)
