# функциюНапишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# * При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
from pathlib import Path


def rename_groupfiles(result_name, extension, folder):
    if Path(folder).exists():
        work_directory = Path(folder)
        for item in enumerate(work_directory.iterdir(), 1):
            number, orig_path = item
            *_, orig_names = str(orig_path).split("\\")
            if "." not in orig_names:
                orig_name, *_ = str(orig_names).split(".")
                type = ""
            else:
                orig_name, *_, type = str(orig_names).split(".")
            make_name = f"{orig_name}_{result_name}_{number}.{extension}"
            if make_name[0:int(len(make_name) / 2)] not in orig_names:
                if ''.join(type) != "py":
                    orig_path.rename(make_name)
            else:
                print(f"в указанной папке файл с таким именем {make_name}")
    else:
            print(f' указанной папки {folder} не существует')


#
rename_groupfiles("sample", "txt", r'C:\teach\pyt\deep_python_home\HW_7\task_7_6')
