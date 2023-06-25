# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона

# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.


import os
import random
import string
from pathlib import Path


def create_files(extension, results, min_name_length=6, max_name_length=30, min_file_size=256, max_file_size=4096, num_files=42):

    Path(results).mkdir(parents=True, exist_ok=True)

    for _ in range(num_files):
        name_length = random.randint(min_name_length, max_name_length)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length))
        file_name += f".{extension}"
        file_size = random.randint(min_file_size, max_file_size)
        data = bytes(random.randint(0, 255) for _ in range(file_size))
        path_to_files = str(Path(results) / file_name)
        with open(path_to_files, 'wb+') as file:
            file.write(data)
        print(f"Создан файл: {file_name}")


def gen_files(name_folder, **kwargs):
    for ext, quanty in kwargs.items():
        create_files(ext,name_folder, num_files=quanty,)




save_result_directory = r'C:\teach\pyt\deep_python_home\HW_7\task_7_4'

if __name__ == '__main__':
    gen_files(save_result_directory,bin=1, exe=1,)
    # create_files('bin', min_name_length=8, max_name_length=15, min_file_size=512, max_file_size=2048, num_files=10)
