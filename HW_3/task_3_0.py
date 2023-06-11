# ✔Создайте вручную список с повторяющимися элементами. 
# ✔Удалите из него все элементы, которые встречаются дважды.

COUNT_NUM = 2

example_list = [6, 7, 1, 1, 9, 2, 2, 2, 6, 4, 4]
print(example_list)
for item in example_list:   
    if example_list.count(item) == COUNT_NUM:
        for i in range(COUNT_NUM):
            example_list.remove(item)
print(example_list)
