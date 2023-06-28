# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из предыдущей задачи. Функция должна извлекать ключи
# словаря для заголовков столбца из переданного файла.


import pickle
import csv


def convert(filename):
    with (open(filename, 'rb') as f_pi,
          open("export.csv", "w", newline='', encoding='utf-8',) as csv_w,
          ):
        picl_load = (pickle.load(f_pi))
        field = []
        rows = []
        for item in picl_load:
            rows.append(item)
            for key in item:
                if key not in field:
                    field.append(key)
        level, id_p, name, hash_name = field
        csv_write = csv.DictWriter(csv_w, fieldnames=[level, id_p, name, hash_name])
        csv_write.writeheader()
        csv_write.writerows(rows)


if __name__ == '__main__':
    convert("person_new.pickle")
