import fractions

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.


def correct_print_fraction(numerator, denominator):
    for i in range(9, 1, -1):
        if numerator % i == 0 and denominator % i == 0:
            numerator /= i
            denominator /= i
    if numerator > denominator:
        whole_part = 0
        temp = numerator
        while whole_part == 0:
            if numerator % denominator == 0:
                whole_part = numerator / denominator
                fin_numerator = temp - numerator
            numerator -= 1
        return f'{int(whole_part)} целых {int(fin_numerator)}/{int(denominator)}'   
    elif numerator == denominator:
        return 1
    else:
        return f'{int(numerator)}/{int(denominator)}'


stroka_1 = '9/5'
stroka_2 = '3/7'
num1, denom1 = map(int, stroka_1.split('/'))
num2, denom2 = map(int, stroka_2.split('/'))
#  сложение дробей с равными знаменителями
if denom1 == denom2:
    sum_num = num1 + num2
    sum_denom = denom1
    print(f'{stroka_1} + {stroka_2} = {correct_print_fraction(sum_num, sum_denom)}')
#  сложение дробей с различными знаменителями
common_denom = denom1 * denom2
sum_num = (num1 * denom2) + (num2 * denom1)
print(f'{stroka_1} + {stroka_2} =  {correct_print_fraction(sum_num, common_denom)}')
# умножение дробей 
multip_num = num1 * num2
multip_denom = denom1 * denom2
print(f'{stroka_1} * {stroka_2} =  {correct_print_fraction(multip_num, multip_denom)} ')

fraction_1 = fractions.Fraction(9,5)
fraction_2 = fractions.Fraction(3,7)
print(f' проверка с использованием модуля fractions')
print(f' {fraction_1} + {fraction_2} = {fraction_1 + fraction_2}')
print(f' {fraction_1} * {fraction_2} = {fraction_1 * fraction_2}') 