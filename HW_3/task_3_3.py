# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

text = input("Ведите текст:").strip().replace(" ", '')
help_list = list(text)
for item in help_list:
    if not item.isalpha():
        help_list.remove(item)
set_uniq = set(help_list)
count_letter = 0
leter_list = []
leter_count = []
dict_result = dict()
for item in set_uniq:
    for letter in help_list:
        if letter == item:
            count_letter += 1
    dict_result[item] = count_letter
    count_letter = 0
print(dict_result)

