# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# Возьмите любую из  задач с прошлых семинаров (например сериализация данных), которые
# вы уже решали. Превратите функции в методы класса, а параметры в свойства. Задачи
# должны решаться через вызов методов экземпляра.


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    pass


class Birds(Animal):
    pass


class Cat(Animal):
    pass


class AnimalFactory:
    all_class = {"cat": Cat, "dog": Dog, "birds": Birds}

    def __init__(self, type_animal, *args, **kwargs):
        self.type_animal = type_animal
        self.__args = args
        self.__kwargs = kwargs

    def create_animal(self):
        for key, item in AnimalFactory.all_class.items():
            if self.type_animal == key:
                return item(*self.__args, **self.__kwargs)
        return None


cats = AnimalFactory("cat", "murzik").create_animal()
dog = AnimalFactory("dog", "Gav").create_animal()
bird = AnimalFactory("birds", "kesha").create_animal()

print(type(cats), cats.name)
print(type(dog), dog.name)
print(type(bird), bird.name)
