class Decorator:
    def __init__(self, min_v, max_v):
        self.min_v = min_v
        self.max_v = max_v

    def __call__(self, func):
        def inner(*args, **kwargs):
            for arg in args:
                if not self.min_v < arg < self.max_v:
                    raise ValueError()
            return func(*args, **kwargs)
        return inner


@Decorator(-5, 0)
def foo(x, y):
    pass


foo(0, 20)
