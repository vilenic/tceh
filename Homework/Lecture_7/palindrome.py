#!/usr/bin/python

import string
from functools import reduce


def stripPunctuation(text):
    """Убирает пунктуацию и специальные символы из строки"""

    newstring = ''
    for ch in text:
        if ch in string.punctuation or ch in "`'\"":
            continue

        newstring += ch

    return newstring


def listTransform(text):
    """Записывает отдельные слова из строки в список"""

    text = text.split(" ")

    return text


def isPalindromeText(text):
    """Проверяет не является ли вся введенная строка палиндромом"""

    if len(text) < 3:
        raise RuntimeError('Your string is too short to be a palindrome')

    text = listTransform(text)
    text = reduce((lambda x, y: x + y), text)

    if text != text[::-1]:
        return False

    return True


def isPalindromeWord(word):
    """Проверяет каждое слово из списка. Возвращает кортеж со словом
    и результатом проверки"""

    if len(word) < 3:
        return (word, False)

    if word != word[::-1]:
        return (word, False)

    return (word, True)


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

    # Если строка целиком не палиндром - бъем ее на слова и пишем их в
    # список
    text = listTransform(text)

    # Список слов проверям на предмет палиндромичности и формируем новый
    # список, который содержит только палиндромы
    check_text = list(filter((lambda x: x[1] is True), map(isPalindromeWord, text)))

    # Если список палиндромов оказывается пустым --> до свидания!
    if len(check_text) == 0:
        print("Unfortunately, there are no palindromes to be found...")
    else:
        printResult(check_text)







