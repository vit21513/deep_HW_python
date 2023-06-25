# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. Известно,
# что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
from random import randint

NUMBERS_QUEENS = 8
pozition = [[5, 3], [4, 1], [7, 2], [5, 2], [5, 5], [8, 2], [7, 7], [3, 6]]


def check_queen(queen_poz):
    for i in range(NUMBERS_QUEENS):
        for j in range(i + 1, NUMBERS_QUEENS):
            if queen_poz[i][0] == queen_poz[j][0] or queen_poz[i][1] == queen_poz[j][1] or \
                    abs(queen_poz[i][0] - queen_poz[j][0]) == abs(queen_poz[i][1] - queen_poz[j][1]):
                return False
    print(queen_poz)
    return True


if __name__ == '__main__':
    print(check_queen(pozition))