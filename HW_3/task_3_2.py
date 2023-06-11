#  Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔Строки нумеруются начиная с единицы. 
# ✔Слова выводятся отсортированными согласно кодировки Unicode.
# ✔Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

text = input("Ведите текст:").replace(".", " ").replace(",", " ").strip()
example = text.split(" ")
example.sort()
max_len_element = 0
for element in example:
    if len(element) > max_len_element:
        max_len_element = len(element)
for item, value in enumerate(example, 1):
    print(f' {item}. {value :>{max_len_element}}')
