# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

example_list = [5, 5, 5, 7, 6, 5, 3, 7, 1, 7, 0, 8]

COUNT_NUM = 2

result =[]
print(f'исходный список {example_list}')
for item in example_list:
    if example_list.count(item) > COUNT_NUM:
        if item not in result:
            result.append(item)
print(f'Cписок повторяющихся элементов {result}')


