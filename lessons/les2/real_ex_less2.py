import csv


class Animal:
    def __init__(self, nickname, age, color):
        self.nickname = nickname
        self.age = age
        self.color = color

    def __str__(self):
        return f'{self,__class__.__name__} {self.nickname}'


class Cat(Animal):
    pass


class Cow(Animal):
    pass


class Animals:
    def __init__(self) -> None:
        self.data = []

    def create_animal(self, type, nickname, age, color):
        if type == 'cat':
            _class = Cat
        elif type == 'cow':
            _class = Cow
        else:
            raise ValueError(f'There is no animal called {type}')
        return _class(nickname, age, color)

    def load_animals(self):
        rows = loader()
        for type, nickname, age, color in rows:
            self.data.append(self.create_animal(type, nickname, age, color))


def loader():
    with open("animals.csv") as f:
        rows = csv.reader(f)
        return [r for r in rows]


if __name__ == '__main__':
    print(loader())
