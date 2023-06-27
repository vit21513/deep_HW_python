# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами 
# и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение/
#  округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла,
# возвращайтесь в его начало.
from pathlib import Path


def multi_func(numbers, names, results, n_files):

    Path(results).mkdir(parents=True, exist_ok=True)
    path_to_files = str(Path(results) / n_files)

    with (
        open(numbers, 'r', encoding='utf-8') as f_numbers,
        open(names, 'r', encoding='utf-8') as f_names,
        open(path_to_files, 'w', encoding='utf-8') as result,
    ):
        len_names = sum(1 for _ in f_names)
        len_numbers = sum(1 for _ in f_numbers)
        f_names.seek(0, 0)
        f_numbers.seek(0, 0)
        for i in range(max(len_numbers, len_names)):
            read_num = f_numbers.readline()
            if read_num =='':
                f_numbers.seek(0,0)
                read_num = f_numbers.readline()
            res_list = read_num.replace('\n', '').split("|")
            read_name = f_names.readline()
            if read_name =='':
                f_names.seek(0,0)
                read_name = f_names.readline()
            res_name = read_name.replace('\n', '')
            multi = int(res_list[0]) * float(res_list[1])
            if multi > 0:
                res = res_name + '|' + str(int(multi))
            else:
                res = res_name.lower() + '|' + str(abs(multi))
            result.write(res+'\n')


path_names = r'C:\teach\pyt\deep_python_home\HW_7\task_7_2\result_2.txt'
path_numbers = r'C:\teach\pyt\deep_python_home\HW_7\task_7_1\result_1.txt'
save_result_directory = r'C:\teach\pyt\deep_python_home\HW_7\task_7_3'
name_files = 'result.txt'
if __name__ == "__main__":
    multi_func(path_numbers, path_names, save_result_directory, name_files)
