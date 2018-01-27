#!/usr/bin/python3

import string

russian_chars = "йцукенгшщзхъфывапролджэячсмитьбюё"

def check_language(text):
    english = 0
    russian = 0
    try:
        for ch in text:
            if ch in string.ascii_lowercase and russian == 0:
                english += 1
            elif ch in russian_chars and english == 0:
                russian += 1
            elif ch in string.whitespace or ch in string.punctuation \
                    or ch in string.digits:
                continue
            else:
                raise RuntimeError
        if english > 0:
            return "Английский"
        else:
            return "Русский"
    except RuntimeError:
        return "error"

def pangramma(text, lang):
    missing_chars = []
    if lang == "Английский":
        for ch in string.ascii_lowercase:
            if ch in text:
                continue
            else:
                missing_chars.append(ch)
    elif lang == "Русский":
        for ch in russian_chars:
            if ch in text:
                continue
            else:
                missing_chars.append(ch)
    return missing_chars

print("Для выхода из программы наберите 'exit'")
while True:

    user_input = input('\nВведите текст для проверки: ')
    user_input = user_input.lower()
    if user_input == "exit":
        exit()

    language = check_language(user_input)
    if language == "error":
        print("С текстом что-то не так! Возможно смешаны \
                кириллица и латиница. Придется повторить...")
        continue
    else:
        result = pangramma(user_input, language)
        print("\nЯзык:", language)
        if result == []:
            print("\nВведенный текст является панграммой! Поздравляем!")
        else:
            print("\nВведенный текст не является панграммой!")
            print("В тексте не хватает следующих букв:")
            print(sorted(result))
