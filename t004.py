# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


import math
a_x = int(input('введите координаты X точки A: '))
a_y = int(input('введите координаты Y точки A: '))
b_x = int(input('введите координаты X точки B: '))
b_y = int(input('введите координаты Y точки B: '))
print('расстояние между точками A и B равно: ', round(math.sqrt((b_x - a_x) ** 2 + (b_y - a_y) ** 2), 2))
    