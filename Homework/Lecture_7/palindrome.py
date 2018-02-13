#!/usr/bin/python

import string
import time
from functools import reduce

# Декораторы по заданию
def first_decorator(func):
    def inner(*args, **kwargs):
        print("First decorator")
        result = func(*args, **kwargs)
        return result
    return inner

def second_decorator(func):
    def inner(*args, **kwargs):
        print("Second decorator")
        result = func(*args, **kwargs)
        return result
    return inner

def third_decorator(func):
    def inner(*args, **kwargs):
        print("Third decorator")
        result = func(*args, **kwargs)
        return result
    return inner

# Функция для теста декораторов
@first_decorator
@second_decorator
@third_decorator
def foo(x, y):
    result = x * y
    return result



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


@timer()
def stripPunctuation(text):
    """Убирает пунктуацию и специальные символы из строки"""

    newstring = ''
    for ch in text:
        if ch in string.punctuation or ch in "`'\"":
            continue

        newstring += ch

    return newstring


@timer()
def listTransform(text):
    """Записывает отдельные слова из строки в список"""

    text = text.split(" ")

    return text


@timer()
def isPalindromeText(text):
    """Проверяет не является ли вся введенная строка палиндромом"""

    if len(text) < 3:
        raise RuntimeError('Your string is too short to be a palindrome')

    text = reduce((lambda x, y: x + y), text)

    if text != text[::-1]:
        return False

    return True


@timer(enabled=False)
def isPalindromeWord(word):
    """Проверяет каждое слово из списка. Возвращает кортеж со словом
    и результатом проверки"""

    if len(word) < 3:
        return (word, False)

    if word != word[::-1]:
        return (word, False)

    return (word, True)


@timer()
def printResult(data):
    """Выводит в консоль результат проверки по словам"""

    print('\nYour string contains following palindromes:')
    cnt = 1
    for i in range(len(data)):
        print("{}: {}".format(cnt, data[i][0]))
        cnt += 1


if __name__ == '__main__':

    text = ''

    while not text:
        text = input("Input your text: ")

    text = text.lower()
    text = stripPunctuation(text)

    # Бъем строку на слова и пишем их в список
    text = listTransform(text)

    try:
        check_text = isPalindromeText(text)
    except RuntimeError as e:
        print(e)
        exit(0)

    # Проверяем не вся ли строка палиндром, чтобы в таком случае не
    # бежать дальше по коду
    if check_text:
        print("Your string is a palindrome")
        exit(0)


    # Список слов проверям на предмет палиндромичности и формируем новый
    # список, который содержит только палиндромы
    check_text = list(filter((lambda x: x[1] is True), map(isPalindromeWord, text)))

    # Если список палиндромов оказывается пустым --> до свидания!
    if len(check_text) == 0:
        print("Unfortunately, there are no palindromes to be found...")
    else:
        printResult(check_text)

    # Тестим декораторы
    decor_test = foo(10, 100)
    print(decor_test)





