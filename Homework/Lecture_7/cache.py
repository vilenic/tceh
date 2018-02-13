#!/usr/bin/python

import time

def timer(enabled=True):
    """Таймер исполнения функций с возможностью вкл/выкл"""
    def decor(func):
        def wrapper(*args, **kwargs):
            if enabled is True:
                start = time.time()
                result = func(*args, **kwargs)
                stop = time.time()
                elapsed = stop - start
                print("{}: {:.6f} seconds".format(func.__name__, elapsed))
            else:
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decor


def cache(func):
    def inner(*args):
        to_cache = tuple([*args])

        if to_cache in cache_dict:
            print("From cache")
            return cache_dict[to_cache]

        result = func(*args)
        cache_dict[to_cache] = result
        print("Function ran")
        return result
    return inner

@timer()
@cache
def calc(x, y):

    result = x * y
    return result

cache_dict = dict()

print(calc(100, 50))
print(calc(100, 50))

print(calc(200, 100))

print(calc(200, 50))

print(calc(200, 100))

