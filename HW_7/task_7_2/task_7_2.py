# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.


import random
from pathlib import Path

list_words = 'уыеэоаяиюэ'
list_words2 = 'цкнгшщзхъждлрпфчсмтб'
max_len = 7
min_len = 4


def fill_name(name, quanty, directory):
    Path(dir).mkdir(parents=True, exist_ok=True)
    path_to_files = str(Path(dir) / name)
    with open(f'{path_to_files}', 'a+', encoding='utf-8') as f:
        for i in range(quanty):
            f.write(("".join(random.choice(list_words2) + random.choice(list_words) for _ in
                             range(random.randint(min_len, max_len) // 2)) + '\n').capitalize())


dir = r'C:\teach\pyt\deep_python_home\HW_7\task_7_2'

if __name__ == "__main__":
    fill_name("result_2.txt", 10, dir)
