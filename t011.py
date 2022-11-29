# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

num = [1.1, 1.2, 3.1, 5, 10.01]
minn = maxx = round(num[0] % 1, 2)
for i in num[1:]:
    tail = round(i % 1, 2)
    if tail == 0:
        continue
    if tail > maxx:
        maxx = tail
    elif tail < minn:
        minn = tail
print(maxx-minn)
