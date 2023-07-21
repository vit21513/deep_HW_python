# Задание №5
# Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта. Класс имеет следующие методы:
# Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
# Метод входа в систему – требует указать имя и id пользователя. Далее метод создает пользователя и проверяет есть ли он в списке пользователей проекта.
# Если в списке его нет, то вызывается исключение доступа. Если пользователь присутствует в списке пользователей проекта, то пользователь,
# который входит получает его уровень доступа и становится администратором.
# Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, чем уровень админа, вызывайте исключение уровня доступа.

# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера


import json

from exception_user import AccessException, LevelException
from user import User


class Project:

    def __init__(self, users):
        self.users = users
        self.admin = None

    @classmethod
    def load(cls, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                users_dict = json.load(f)
        except Exception as e:
            print(f'При открытии файла {filename} возникла ошибка {e}. ')
        else:
            # print(f'{users_dict = }')
            users = []
            for level, user in users_dict.items():
                for user_id, name in user.items():
                    users.append(User(user_id, name, level))

            return Project(users)

    def __str__(self):
        return str(self.users)

    def set_admin(self, user_id, name, level):
        self.admin = User(user_id, name, level)
        return User(user_id, name, level)
    # вход в систему
    def login(self, user_id, name):
        user_new = User(user_id, name)
        if user_new not in self.users:
            raise AccessException(user_id)
        for user in self.users:
            if user_new == user:
                self.admin = user
        return "Logging sucsess"

    # добавление пользователя
    def add_user(self, user_id, name, level):
        if int(self.admin.level) >= int(level):
            raise LevelException(level, name)
        self.users.append(User(user_id, name, level))
        return "User added"


if __name__ == '__main__':
    filename = 'users.json'
    project = Project.load(filename)
    project.login('359', 'Алексей')
    print(project.admin)
    project.add_user('010', 'Мустафа', 7)
    print(*project.users)
