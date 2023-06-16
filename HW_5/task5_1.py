# напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

from unittest.mock import patch


example = 'C:/teach/алгоритм/home_work_python/home_work_python/HW_leson1/task1.py'


def patch_split(input_str):
   
    *patch, files_name,type_files =  example.replace('/','.').split('.')
    patch = "/".join(patch)
    return patch, files_name, type_files


print(patch_split(example))