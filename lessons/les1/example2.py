class Example:
    attr = "hello"

    def print_attr(self):
        print(self.attr)


def print_attr(self):
    print(self.attr)


ExampleTwo = type('ExampleTwo', (object,), {
                  'attr': 'Hello', "print_attr": print_attr})
print(ExampleTwo)
