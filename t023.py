# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# первый вариант

one = 6782
x = sum(int(i) for i in str(one) if i.isdigit())
print(x)


# второй вариант


a = 6782
b = 0.056
x = lambda num: sum(int(i) for i in str(num) if i.isdigit())       # generator object
result = [x(i) for i in (a,b)]
print(result)