# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
day = int(input('Ведите число дня недели:'))
if day > 0 and day <= 7:
    if day > 0 and day <= 5:
        print('рабочие дни')
    else:
        print('выходной')
else:
    print('нет такого дня недели')