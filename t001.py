# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# day = int(input('Ведите число дня недели:'))
# if day > 0 and day <= 7:
#     if day > 0 and day <= 5:
#         print('рабочие дни')
#     else:
#         print('выходной')
# else:
#     print('нет такого дня недели')


# day = int(input("Введите день недели  : "))
# if 0 < day < 8:
#     if day == 6 or day == 7:
#         print('выходной')
#     else:
#         print('будни')
# else:
#     print("введите другой день недели")

day = int(input("Введите день недели  : "))
match day:
    case 1:
        print('понедельник')
    case 2:
        print('вторник')
    case 3:
        print('среда')
    case 4:
        print('четверг')
    case 5:
        print('пятница')
    case 6:
        print('суббота')
    case 7:
        print('воскресенье')
    case _:
        print('не такого дня')