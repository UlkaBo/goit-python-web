class DocType(type):
    def __new__(self, name, bases, dict):
        for key, value in dict.items():
            if key.startswith("__"):
                continue
            if not getattr(value, "__call__"):
                continue
            if not getattr(value ,"__doc__"):
                raise TypeError()
        return type.__new__(self, name, bases, dict)


class Animal(metaclass=DocType):
    def eat(self):
        # """
        # I am doing just nothing and it is fine!
        # """
        pass
