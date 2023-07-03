# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import json
import os
import random
from math import sqrt


def gen_csv(num=3, start_num=1, end_num=100, quantity_min=100, quantity_max=1000):
    with open("randomlist.json", "w", encoding="utf-8") as js:
        json.dump([[random.randint(start_num, end_num) for _ in range(num)] for _ in
                   range(random.randint(quantity_min, quantity_max))], js)


def save_vareables(func):
    def wrapper(*args, **qargs):
        if os.path.exists(func.__name__ + ".json"):
            with open(func.__name__ + ".json", "r", encoding='utf-8') as res_f:
                res = json.load(res_f)
        else:
            res = []
        res.append({"args": [*args, *qargs], "result": (func(*args, **qargs))})
        with open(func.__name__ + ".json", "w", encoding='utf-8') as result_f:
            json.dump(res, result_f, indent=1)
        return func
    return wrapper


def csv_variable(func):
    """ function reads json file and passes the values of variables to the function"""
    if os.path.exists("randomlist.json"):
        with open("randomlist.json", encoding='utf-8') as res_f:
            for item in json.load(res_f):
                func(*item)
            return func
    else:
        return func


@csv_variable
@save_vareables
def check(a, b, c):
    """ function return value of ax² + bx + c = 0 """
    disc = b * b - 4 * a * c
    if disc < 0:
        return False
    else:
        root = sqrt(disc)  # вычисляем корень
        x_1 = (-b + root) / (2 * a)  # вычисляем первое решение
        if disc != 0:  # проверяем, существует ли другое решение
            x_2 = (-b - root) / (2 * a)  # вычисляем второе решение
            return x_1, x_2
        else:
            return x_1


# gen_csv()
check(5, 0, -5)
check(45,7,90)
check(5,7,9)
