# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# (Вывод тех элементов, которые были без повторов)
# Ввод: 1 2 3 2 4 4
# Вывод: 1 3


order = [1, 2, 3, 2, 4, 4]

answer = []
deleted = []

for item in order:
    if item in deleted:
        continue
    if item in answer:
        deleted.append(answer.pop(answer.index(item)))
    else:
        answer.append(item)

print(answer)















# my_list = list(map(int, input('введите числа через пробел: \n').split()))
# print(f'исходный список:{my_list}')
# new_list = []
# [new_list.append(i)for i in my_list if i not in new_list]
# print(f"Список из неповторяющихся элементов: {new_list}")
