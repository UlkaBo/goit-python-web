class Example:
    __slots__ = ('age',)


e = Example()
e.age = 'one'
print(e.age)
print(getattr(e, 'age'))
