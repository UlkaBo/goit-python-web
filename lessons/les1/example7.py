def class_decorator(cls):
    class MaineCoon(cls):
        def print_message(self):
            print('I am MAineCoon')
    return MaineCoon


@class_decorator
class Cat:
    pass


Cat().print_message()
