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
                print("Operation took {:.6f} seconds".format(elapsed))
            else:
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decor


def cache(func):
    def inner(*args):
        print("-" * 100)

        if args in cache_dict:
            print("From cache")
            return cache_dict[args]

        result = func(*args)
        cache_dict[args] = result
        print("Function ran")
        return result

    return inner

@timer()
@cache
def calc(x, y):
    result = x * y
    return result

cache_dict = dict()

print("Result:", calc(100, 50))
print("Cache: {}".format(cache_dict))

print("Result:", calc(100, 50))
print("Cache: {}".format(cache_dict))

print("Result:", calc(200, 100))
print("Cache: {}".format(cache_dict))

print("Result:", calc(200, 50))
print("Cache: {}".format(cache_dict))

print("Result:", calc(200, 100))
print("Cache: {}".format(cache_dict))
