class DocType(type):
    def __new__(self, name, bases, dic):
        for k,v in dic.items():
            print(k,v)
            if not getattr(v, '__doc__'):
                raise TypeError()
        return type.__new__(self, name, bases, dic)

class Animal(metaclass = DocType):
    def eat(self):
        '''
        i am
        '''
        pass

Animal()