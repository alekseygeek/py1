# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# F−n = (−1)n+1 * Fn
# F−1 = 1,
# F−2 = -1,
# Fn = F(n+2)−F(n+1).


# num = 8
# right = [0, 1]
# left = [0, 1]
# for i in range(2, num + 1):
#     right.append(right[i-1]+right[i-2])
#     left.append(left[i-2]-left[i-1])
# # print(left)
# left.reverse()
# # print(left)
# left.extend(right)
# print(left)

def get_fibonacci(n):
    fib_list = []
    a, b = 1, 1
    for i in range(n-1):
        fib_list.append(a)
        a, b = b, a+b
    a, b = 0, 1     
    for i in range(n):
        fib_list.insert(0, a)
        a, b = b, a-b
    return fib_list

n = int(input('введите число: '))+1
fib_list = get_fibonacci(n)
print(fib_list)
