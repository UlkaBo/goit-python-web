#from examples.example7 import class_decorator


class Meta(type):

    def __new__(cls, future_class_name, future_class_parents, future_class_atrrs):
        future_class_atrrs['class_number'] = Meta.children_number
        Meta.children_number += 1
        return type(future_class_name, future_class_parents, future_class_atrrs)


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


#print(Cls1, dir(Cls1))
#print(Cls1.class_number, Cls2.class_number)
assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
#print(a, dir(a))
#print(a.class_number, b.class_number)
# print(Meta.children_number)
assert (a.class_number, b.class_number) == (0, 1)