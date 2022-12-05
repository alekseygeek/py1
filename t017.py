# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл (или вывести в терминал) многочлен степени k.
# Пример:
# - k = 2  => 2*x² + 4*x + 5
# - k = 3  => 41*x^3 + 6*x² + 2*x + 98
import random as rd


def dev(k):
    polinom = ''
    for i in range(k, -1, -1):
        prefix =rd.randint(0, 100)
        # print(prefix)
        if prefix != 0:
            if i == 0:
                polinom += ' + ' + str(prefix)
            elif i == 1:
                polinom += ' + ' + str(prefix) + '*x'
            else:
                polinom += ' + ' + str(prefix) + '*x**' + str(i)
    if not polinom:
        polinom = '0'
    return polinom.lstrip(' + ')   # обрезание строки

k = int(input('Введите натуральную степень k ='))
answer = dev(k)
with open('gen_file.txt', 'w') as f:
     f.write(answer)
print(answer)



















# import random as rd
# def dev(k):
#     polinom = ''
#     for i in range(k, -1, -1):
#         if i == 0:
#             polinom += ' + ' + str(rd.randint(0, 100))
#         elif i == 1:
#             polinom += ' + ' + str(rd.randint(0, 100)) + '*x'
#         else:
#             polinom += ' + ' + str(rd.randint(0, 100)) + '*x**' + str(i)
#     return polinom.lstrip(' + ')

# k = int(input('Введите натуральную степень k ='))
# with open('gen_file.txt', 'w') as f:
#     f.write(dev(k))
# print(dev(k))






# import random as rd


# def dev(k):
#     polinom = ''
#     for i in range(k+1):
#         if i == 0:
#             polinom += str(rd.randint(1, k)) + '*x**' + str(k - i)
#         elif i == k:
#             polinom += '+' + str(rd.randint(1, k))
#         else:
#             polinom += '+' + str(rd.randint(1, k)) + '*x**' + str(k-i)
#     return polinom


# k = int(input('Введите натуральную степень k ='))
# with open('gen_file.txt', 'w') as f:
#     f.write(dev(k))
# print(dev(k))
