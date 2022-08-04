ROWS = 4
COLS = 4 # размеры поля игры
A = [
    [" ", 0, 1, 2],
     [0, '-', '-', '-'],
     [1, '-', '-', '-'],
     [2, '-', '-', '-']
]  # Стартовое поле

print("Начнем игру в Крестики-Нолики! Игру начинают Крестики.")

for i in range(ROWS):
   for j in range(COLS):
       print(A[i][j], end = " ")
   print() # Демострация стартового поля

def ask():
    while True:
        cords = input("Введите квадрат для вашего хода № строки, а затем № столбца через пробел, например, 1 0:").split()

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

        if A[x + 1][y + 1] != "-":
            print(" Клетка занята! ")
            continue

        return x, y

def win():
    win_cord = (((1, 1), (1, 2), (1, 3)), ((2, 1), (2, 2), (2, 3)), ((3, 1), (3, 2), (3, 3)),
                ((1, 3), (2, 2), (3, 1)), ((1, 1), (2, 2), (3, 3)), ((1, 1), (2, 1), (3, 1)),
                ((1, 2), (2, 2), (3, 2)), ((1, 3), (2, 3), (3, 3)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(A[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

num = 0
while True:
    step = list(ask())
    if num % 2 != 0:
        A[step[0] + 1][step[1] + 1] = '0'
        num +=1
        for i in range(ROWS):
            for j in range(COLS):
                print(A[i][j], end=" ")
            print()
    else:
        A[step[0] + 1][step[1] + 1] = 'X'
        num +=1
        for i in range(ROWS):
            for j in range(COLS):
                print(A[i][j], end=" ")
            print()
    if win():
        break


    if num == 9:
        print(" Ничья!")
        break