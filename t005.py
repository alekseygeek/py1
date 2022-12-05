# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input('введите число N :'))
# answer = []
# number1 = 1
# for i in range(1, number+1):
#     number1 *= i
#     answer.append(number1)
# print(answer)

# второй вариант

num = int(input())
m = 1
mass = []
for i in range(1, num+1):
    m = m*i
    mass.append(m)
print(mass)
