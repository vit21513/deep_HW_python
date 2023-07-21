# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import json
from project_main import Project
from user import User
import pytest


@pytest.fixture
def load_list_person(filename="users.json"):
    list_person = Project.load(filename)
    list_person.set_admin(user_id="999", name="Владимир", level=4)
    return list_person


def test_add(load_list_person):
    assert load_list_person.add_user(user_id="569", name="Petr", level=5) == "User added"


def test_login(load_list_person):
    assert load_list_person.login(user_id="456", name="Антон") == "Logging sucsess"


def test_admin(load_list_person):
    assert load_list_person.set_admin(user_id="569", name="Petr", level=5) == User(user_id="569", name="Petr", level=5)


if __name__ == '__main___':
    pytest.main()
