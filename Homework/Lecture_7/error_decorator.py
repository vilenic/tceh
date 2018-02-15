#!/usr/bin/python

import string
import sys
import traceback

class Error(Exception):
    pass

class RightError(Error):

    def __init__(self, message, expression=''):
        self.message    = message
        self.expression = expression

class WrongError(Error):

    def __init__(self, message, expression=''):
        self.message    = message
        self.expression = expression


def error_catcher(func):
    def inner(*args):
        try:
            func(*args)
        except RightError:
            print(sys.exc_info())
        except Exception:
            raise WrongError('WrongError: Very wrong') from None
    return inner


@error_catcher
def foo():
    user_input = input("Hi, please input: ")
    if user_input[0] in string.ascii_lowercase:
        raise RuntimeError(user_input, 'Something went wrong')
    elif user_input[0] in string.ascii_uppercase:
        raise RuntimeError(user_input, 'Something is weird')
    elif user_input[0] in string.digits:
        raise RightError('Something right just happened')



if __name__ == '__main__':

    foo()

