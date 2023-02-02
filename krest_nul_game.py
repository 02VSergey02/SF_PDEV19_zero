# Задаем поле игры ввиде списка и как храним инф о состоянии клеток

#field = [" "] * 9 " ",
#field[" ", " ", " ", " ", " ", " ", " ", " ", " "]
#field[" " for i in range(9)]

# field = [" "] * 9
# field[2] = "X"
# field
# [' ', ' ', 'X', ' ', ...]

field = [[" "] * 3 for i in range(3) ] #создаем поле с пом 2х мерн списка


def show(): # функция показыват вывод игрового поля
    print(f"  0 1 2") # индексы

    for i in range(3): # само поле. циклом по списку
        row_info = " ".join(field[i])

        print(f"{i} {row_info}")

show()


def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


ask()
# 30:56 пишем прототип
num = 0  # перемен номер хода (свего - 9)
while True:
    num +=1 # на кажд итерации увелич на 1
    show()
    if num % 2 == 1:
        print("Ходит крестик ")
    else:
        print("Ходит нолик ")

    x, y = ask() # x,y ранее return

    if num % 2 == 1:
        field[x][y] = "x"
    else:
        field[x][y] = "0"
# тестирование на ничью

    if num == 9:
        break
        print("Ничья ")




