# Создайте программу для игры в ""Крестики-нолики".


def show_field(arr: list):
    print(" _"*9 + "\n", f"{arr[0]} \t {arr[1]} \t {arr[2]}")
    print(" _"*9 + "\n", f"{arr[3]} \t {arr[4]} \t {arr[5]}")
    print(" _"*9 + "\n", f"{arr[6]} \t {arr[7]} \t {arr[8]}")
    print(" _"*9)


def check_win(simb: str, arr: list):
    variants = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8), (2, 4, 6), (0, 4, 8),)
    for i in variants:
        for j in i:
            if (arr[j] == simb):
                continue
            else:
                break
        else:
            return True
    return False


def draw(arr: list):
    for i in range(1, 10):
        if i in arr:
            return False
    return True


if __name__ == "__main__":
    array = list(range(1, 10))
    x = chr(10060)
    o = chr(11093)
    xo = x
    show_field(array)

    while True:
        move = int(input(f'Ход{xo}:'))
        if move in array:
            array[move-1] = xo
            show_field(array)
            if check_win(xo, array):
                print(f"{xo} победили")
                break
            elif draw(array):
                print(f"ничья!")
                break
            xo = x if xo == o else o
        else:
            print('Неверный ввод.Попробуйте ещё раз.')
        continue
