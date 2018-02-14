#!/usr/bin/python



def check(func):
    def inner(*args):
        print("-" * 50)
        print('The folowing arguments were given: {}\n'.format(args))
        result = func(*args)
        for el in args:
            print(el, "is of type:", type(el), "\n")
        print("The folowing result has been achieved: {}\n".format(result))
        print("Result is of type:", type(result), "\n")
        return result
    return inner


@check
def foo(*args):
    return args * 2


@check
def multiply(x, y):
    return x * y


if __name__ == '__main__':

    a = foo((1, 2), "aaa")

    b = multiply(10, 40)


