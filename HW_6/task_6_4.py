import task_6_3 as queen
from random import randint

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок


def random_poz_queen():
    res = [[randint(1, 9) for i in range(2)] for i in range(queen.NUMBERS_QUEENS)]
    for i in range(len(res)):
        if res.count(res[i]) >= 2:
            for j in range(res.count(res[i])):
                res[res.index(res[i])] = [randint(1, 9) for i in range(2)]
    return res


if __name__ == "__main__":
    index = 0
    while index < 4:
        if queen.check_queen(random_poz_queen()):
            index += 1
