# Возьмите любую из задач с прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.
import os
from random import randint, uniform
from pathlib import Path


class Fill_file:
    minim = -1000
    maxim = 1000

    # можно было  __init__ не делать передавать сразу в функцию, сделал для учебных целей
    def __init__(self, name, quanty, directory):
        self.name = name
        self.quanty = quanty
        self.dir = directory

    def generate(self):
        Path(self.dir).mkdir(parents=True, exist_ok=True)
        path_to_files = Path(self.dir) / self.name
        with open(f'{path_to_files}', 'a+', encoding='utf-8') as f:
            for _ in range(self.quanty):
                print(f'{str(randint(Fill_file.minim, Fill_file.maxim))}|'
                      f'{str(uniform(Fill_file.minim, Fill_file.maxim))}', file=f)


if __name__ == "__main__":
    sample = Fill_file('result_1.txt', 100, os.getcwd())
    sample.generate()
