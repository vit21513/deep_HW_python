# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from task_6_1.thrid import input_data
from sys import argv

_, *date = argv
print(input_data(*date))
