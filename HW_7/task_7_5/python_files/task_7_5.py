from pathlib import Path
# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.


import os
import shutil
from pathlib import Path


def sort_files(sort_dir, choise_sort: dict):
    work_directory = Path(sort_dir)
    for folder in choise_sort:
        (work_directory / folder).mkdir(parents=True, exist_ok=True)
    dict_files = dict()
    for item in work_directory.iterdir():
        if item.is_file() and str(item).find('.', 0) > 0:
            dict_files[item] = str(item)[str(itecm).find('.'):]
    for path_files, type_files in dict_files.items():
        for folder, extension in choise_sort.items():
            if type_files in extension:
                try:
                    shutil.move(path_files, work_directory / folder)
                except:
                    print(f' В указанной папке {folder} файл {path_files} уже существует')


input_patch = r'C:\teach\pyt\deep_python_home\HW_7\task_7_5'

must_sorted = {"videos": [".mp4", ".avi", ".mkv"], "images": [".jpg", ".png", ".gif"],
               "text": [".txt", ".doc", ".pdf"]}

sort_files(input_patch, must_sorted)
