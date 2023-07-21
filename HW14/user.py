# Вспомните задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7).
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Реализуйте магический метод проверки на равенство пользователей

import json


class User:
    def __init__(self, user_id, name, level=None):
        self.user_id = user_id
        self.name = name
        self.level = level

    def __str__(self):
        return f'Пользователь\t Идентификационный номер: {self.user_id},\t имя: {self.name},\t уровень доступа: {self.level}\n'

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name


    def add_user_to_file(filename):

        try:
            with open(filename, "r", encoding="utf-8") as f:
                my_dict = json.load(f)
        except Exception:
            my_dict = {str(level): {} for level in range(1, 8)}
        print(f'{my_dict = }')
        while True:
            name, user_id, level, *_ = input(
                "Введите имя, личный идентификатор и уровень доступа через пробел: ").split()
            try:
                if user_id not in my_dict[level].keys():
                    my_dict[level].update({user_id: name})
                    break
                else:
                    print('Идентификатор не уникален')
            except KeyError as e:
                print(f'Ошибка ввода уровня {e}')
        print(f'{my_dict = }')
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(my_dict, f, indent=1, ensure_ascii=False)




if __name__ == '__main__':

    User.add_user_to_file("users.json")