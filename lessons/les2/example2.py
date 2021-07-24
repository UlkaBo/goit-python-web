import csv
import json


# global variable ########
FILE_FORMAT = "json"
ALL_ANIMAL_CLASSES = {}
##########################

# decorator for class
def register(cls):
    ALL_ANIMAL_CLASSES[cls.__name__] = cls
    return cls

class Animal:
    __slots__ = ("name", "age", "color")

    def __init__(self, nickname, age: int, color) -> None: 
        self.nickname = nickname
        self.age = age
        self.color = color

    def method(self):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__} {self.nickname}"

@register
class Cat(Animal):
    pass

# @register
class Cow(Animal):
    pass


class LoaderInterface:
    def load(self, file_name):
        raise NotImplementedError()


class CSVLoader(LoaderInterface):
    def load(self, file_name):
        with open(f"lection2/data/{file_name}") as f:
            rows = csv.reader(f)
            return [r for r in rows]


class JSONLoader(LoaderInterface):
    def load(self, file_name):
        with open(f"lection2/data/{file_name}") as f:
            rows = json.load(f)
            return [r.values() for r in rows]

# meta class
def add_loader(name, bases, attrs):
    if FILE_FORMAT == "csv":
        attrs["loader"] = CSVLoader
    else:
        attrs["loader"] = JSONLoader
    return type(name, bases, attrs)


class Animals(metaclass=add_loader):
    def __init__(self):
        self.data = []
    
    def print_animals(self):
        for a in self.data:
            print(a)
    
    def create_animal(self, type, nickname, age, color):
        if type.lower() == "cat":
            _class = Cat
        elif type.lower() == "cow":
            _class = Cow
        else:
            raise ValueError(f"There is no animal called: {type}")
        return _class(nickname, age, color)

    def load_animals(self, file_name):
        rows = self.loader().load(file_name)
        for type, nickname, age, color in rows:
            self.data.append(self.create_animal(type, nickname, age, color))


if __name__ == "__main__":
    a = Animals()
    a.load_animals("animals.json")
    a.print_animals()
    print(ALL_ANIMAL_CLASSES)

