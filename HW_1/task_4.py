from random import randint

# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.


MAX_COUNT = 10


def find_random_nymber(count_q=MAX_COUNT):
    number = randint(1, 1001)
    print(number, count_q)
    print('Вам нужно угадать число загаданное от 1  до 1000')
    while count_q >= 1:
        print(f'Осталось {count_q} попыток')
        num = input("Введите целое число от 1 до 1000: ")
        if num.strip().isdigit() and int(num) <= 1000:
            num = int(num)
            if num == number:
                print(f'вы угадали  загаданное число {number}')
                break
            elif num > number:
                print(f"Ваше число больше загаданного")
            elif num < number:
                print(f"Ваше число меньше загаданного")
            count_q -= 1
        else:
            print('Вы ввели некоректное число')
    if count_q == 0:
        print("Все попытки исчерпаны, вы проиграли..... ")


find_random_nymber()
