# ✔Функция получает на вход список чисел и два индекса. 
# ✔Вернуть сумму чисел между между переданными индексами.
# ✔Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.


def sum_index_number(list_num, index_one, index_two):
    max_index = max(index_one, index_two)
    min_index =min(index_one, index_two)
    if max_index >= len(list_num):
        max_index = len(list_num)-1
    selection = []
    for i in range(min_index, max_index+1):
        selection.append(list_num[i])
    result= sum(selection)
    return result
    



numbers = [5, 6, 6, 1, 2, 8, 9, 1]

print(sum_index_number(numbers,100, 3))
print(sum_index_number(numbers,0, 4))