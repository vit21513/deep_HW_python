# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
#
from pathlib import Path
from random import uniform, randint

Min = -1000
Max = 1000


def fill_file(name, quanty, dir,):
    Path(dir).mkdir(parents=True, exist_ok=True)
    path_to_files = str(Path(dir) / name)
    with open(f'{path_to_files}', 'a+', encoding='utf-8') as f:
        for _ in range(quanty):
            print(f'{str(randint(Min, Max))}|{str(uniform(Min, Max))}', file=f)


directory = r'C:\teach\pyt\deep_python_home\HW_7\task_7_1'

if __name__ == "__main__":
    fill_file("result_1.txt", 10, directory)

