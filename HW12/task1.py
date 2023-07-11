# Решить задания, которые не успели решить на семинаре.
# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv
import os
import random


class Check:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):

        if isinstance(value, str):
            alph = {"а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                    "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"}
            for item in value.split():
                if item != item.title() or not set(item.lower()).issubset(alph):
                    raise ValueError("All Names must Is Title and only words")
            setattr(instance, self.name, value)


class Student:
    name = Check()
    __max_estimation = 5
    __min_estimation = 2
    __max_quanty_estimation = 7
    __min_balls = 0
    __max_balls = 100

    def __init__(self, name):
        self.name = name
        self.average_ball = self.__average_ball()
        self.average_estimation = self.__average_estimation()

    def __str__(self):
        return f'{self.name}'

    def __load_csv(self):
        os.chdir(os.getcwd())
        if os.path.exists(self.name + ".csv"):
            with open(self.name + ".csv", "r", newline='', encoding='utf-8') as csv_read:
                reader = csv.DictReader(csv_read)
                value_dict = dict()
                for item in reader:
                    value_dict.update(item)
                for key, value in value_dict.items():
                    value_dict[key] = list(map(int, value.replace('[', '').replace("]", '').split(",")))
                return value_dict
        # Здесь случайно генерируются оценки и балы для студента и записываются  файл
        sciences = ["Русский язык", "Математика", "Биология", "Химия", "История", "Черчение"]
        result = dict()
        for item in sciences:
            result.update({item: [[random.randint(Student.__min_estimation, Student.__max_estimation) for _ in
                                   range(Student.__max_quanty_estimation)],
                                  [random.randint(Student.__min_balls, Student.__max_balls) for _ in
                                   range(Student.__max_quanty_estimation)]]})
        with open(self.name + ".csv", 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, quoting=csv.QUOTE_NONNUMERIC, fieldnames=[item for item in sciences])
            writer.writeheader()
            writer.writerows([result])
        return self.__load_csv()

    def __average_ball(self):
        avg_bals = dict()
        for keys, values in Student.__load_csv(self).items():
            temp_list = [val for val in values if val > 5]
            avg_bals[keys] = round(sum(temp_list) / len(temp_list), 0)
        return avg_bals

    def __average_estimation(self):
        avg_estimation = []
        for values in Student.__load_csv(self).values():
            temp_list = [val for val in values if val <= 5]
            avg_estimation.append(round(sum(temp_list) / len(temp_list), 0))
        return round(sum(avg_estimation) / len(avg_estimation), 0)


student1 = Student("Иванов Петр Сергеевич")
student2 = Student("Петрова Мария Сергеевна")
print(f'Студент по фамилии {student1}')
print(f'Средний бал по  тестам : {student1.average_ball}')
print(f'Средняя оценка в разрезе всех  предметов: {student1.average_estimation}')
print(f'Студент по фамилии {student2}')
print(f'Средний бал по предметам: {student2.average_ball}')
print(f'Средняя оценка в разрезе всех  предметов: {student2.average_estimation}')
