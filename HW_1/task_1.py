# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.


def check_quanty_digits(num):
    if 1 <= num <= 999:
        res_len = 0
        while num > 1:
            num = num / 10
            res_len += 1
        return res_len
    else:
        return f"вы ввели некоректное число"


print(check_quanty_digits(123))


# Для цифры верните её квадрат, например 5 - 25


def multi_num(num):
    return num ** 2


print(multi_num(5))


# Для двузначного числа произведение цифр, например 30 - 0

def multiplication_two_digits(num):
    return f'{num % 10} * {num // 10} = {(num % 10) * (num // 10)}'


print(multiplication_two_digits(98))


# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

def reverse_numbers():
    number = input("Введите трехзначное число: ")
    if number.isdigit() and 100 <= int(number) <= 999:
        number = int(number)
        first = number // 100
        thrind = number % 10
        second = number // 10 - first * 10
        print(thrind * 100 + second * 10 + first)
    else:
        print('не корректное число')
        reverse_numbers()


reverse_numbers()


# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.


def table_multiplication():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f'{i}*{j}={i * j}')
        print()


table_multiplication()
