# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.


class Except_personal(Exception):
    pass


class LevelException(Except_personal):

    def __init__(self,level):

        self.level = level

    def __str__(self):
        return f'level {self.level} incorrect'


class AccessException(Except_personal):

    def __str__(self):
        return f'access denied'

