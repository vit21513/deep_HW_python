# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import argparse
from pathlib import Path
import logging
from collections import namedtuple

logging.basicConfig(filename="dir_info.log", filemode='w', encoding='utf-8', level=logging.INFO)
loger = logging.getLogger(__name__)


def inspect_folder(path_folder):
    result = []
    for root, dirs, files in os.walk(Path(path_folder)):
        for file in files:
            if "." not in file:
                orig_name = file
                type_files = "unknown"
            else:
                orig_name, *_, type_files = file.split(".")
            result.append({'name_o': orig_name, 'type': type_files, 'parent_directory': root})
            loger.info(f'name_o: {orig_name}, type: {type_files}, parent_directory: {root}')
        result.append({'name_o': dirs, 'type': 'directory', 'parent_directory': os.path.dirname(root)})
        loger.info(f'name_o: {dirs},type: directory,parent_directory: {os.path.dirname(root)}')
    return create_numtuple(result)


def pars_path():
    parser = argparse.ArgumentParser(prog="creaty named tuple from directory")
    parser.add_argument('-p', metavar='p', default=os.getcwd())
    args = parser.parse_args()
    return inspect_folder(f'{args.p}')


def create_numtuple(list_files):
    result_list = list()
    ObjectDirectory = namedtuple('ObjectDirectory', 'name type parent_directory')
    for obj in list_files:
        name_obj, type_jbj, parent_dir = obj.values()
        result_list.append(ObjectDirectory(name_obj, type_jbj, parent_dir))
    return result_list


if __name__ == "__main__":
    for item in pars_path():
        print(item)
