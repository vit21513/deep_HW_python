# ✔Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения. 
# ✔Вычислите итоговую# прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.



from pickle import TRUE


example = {"Путь Ильича":[23000, -10000, 45000, -12700],
           "Светлый путь":[123000, 500000, 23000, 93000],
           "Вектор":[6000,12000,35000,-12000], 
           }


def sort_company(dict_company: dict):
    sum_cash =dict()
    for item in dict_company:
        sum_cash[item] = sum(dict_company.get(item))
    if all(map(lambda x: x > 0, sum_cash.values())):
        return True
    return False  

print(sort_company(example))