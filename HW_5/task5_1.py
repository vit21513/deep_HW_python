# напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


example = "C:/teach/алгоритм/home_work_python/home_work_python/HW_leson1/task1.py"


def patch_split(input_str):
    *patch_example, files_name, type_files = input_str.replace("/", ".").split(".")
    patch_example = "/".join(patch_example)
    return patch_example, files_name, type_files


print(patch_split(example))
