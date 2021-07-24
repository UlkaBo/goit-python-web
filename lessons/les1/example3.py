def meta_func(name_base, attrs):
    attrs['additional_attr'] = 42
    return type(name, base, attrs)


class Example(metaclass=meta_func):
    attr = "hello"

    def print_attr(self):
        print(self.attr)

# don-t work
