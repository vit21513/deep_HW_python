# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление.Функцию hex используйте для проверки своего результата.

number = input('Введите число:')
if number.isdigit():
    result = []
    digits = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
    number = int(number)
    print(f'Для проверки работы алгоритма число {number} в 16-ой системе = {hex(number)}')
    while number > 0:
        temp = number % 16
        if temp > 9:
            for i in digits.keys():
                if number % 16 == i:
                    temp = digits.get(i)
        result.append(temp)
        number //= 16
    number_hex = "0x"+''.join(str(content) for content in result)[::-1]
    print(number_hex)
else:
    print('некорректный ввод')