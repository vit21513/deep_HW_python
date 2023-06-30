#
# Прочитайте созданный в прошлом задании csv файл без использования
# csv.DictReader. Распечатайте его как pickle строку.

import csv
import pickle


def convert_csv(csv_file, filename):
    with (open(filename, 'bw') as f_pi,
          open(csv_file, "r", newline='', encoding='utf-8', ) as csv_w,
          ):
        list_csv = []
        read = csv.reader(csv_w)
        for item in read:
            list_csv.append(item)
        pickle.dump(list_csv, f_pi)
    with open(filename, 'br') as f_pi:
        # print(pickle.load(f_pi))
        print(*f_pi)


if __name__ == '__main__':

    convert_csv("export.csv","reedit_csv.pickle")
