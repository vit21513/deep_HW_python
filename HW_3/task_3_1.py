# Создайте вручную список с повторяющимися целыми числами.
# ✔Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔Нумерация начинается с единицы.

example_list = [3, 8, 8, 4, 9, 6, 9, 2, 5]
new_list = []
for i, value in enumerate(example_list, 1):
    if value % 2 != 0:
        new_list.append(i)
print(new_list)
