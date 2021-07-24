class MyMeta(type):
    def __init__(self, *args):
        print("Object is initialized")

    def __new__(self, *args):
        print("Object is created")
        return type.__new__(self, *args)


class Example(metaclass=MyMeta):
    pass
