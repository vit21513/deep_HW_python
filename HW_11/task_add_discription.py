# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

import time


class Mystr(str):
    """This class  extends the capabilities class 'str'
    and save creaty objects class

    Args:
        str : any
        str : name any
    """
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.value = value
        instance.time_creaty = time.time()
        return instance

    def __str__(self) -> str:
        """This function return object to string"""
        return f"значение = {self.value} имя = {self.name} время создания {self.time_creaty}"


sample = Mystr("temp1", "petr")
sample2 = Mystr("4oopS", "masha")
print(sample.name, " ", sample.time_creaty, sample.value)
help(sample)
print(Mystr.__doc__)


class Arhive:
    """This class include two values number and string"""

    arch_str = []
    arch_num = []

    def __init__(self, number, stroka):
        """this function create object class Archive and save content another object class"""
        self.number = number
        self.stroka = stroka
        Arhive.arch_str.append(stroka)
        Arhive.arch_num.append(number)

    def __str__(self):
        """This function return object to string"""
        return f"экземпляр класса {Arhive} {self.number =} {self.stroka =}"

    def __repr__(self):
        """This  function return info for devoloper"""
        return f"{Arhive} {self.number =} {self.stroka =}"


one = Arhive(12, "Try class")
print(Arhive.arch_num, Arhive.arch_str)
two = Arhive(34, "another class")
print(Arhive.arch_num, Arhive.arch_str)
three = Arhive(45, "good")
print(Arhive.arch_num, Arhive.arch_str)
print(repr(one))
help(Arhive)
print(Arhive.__doc__)
