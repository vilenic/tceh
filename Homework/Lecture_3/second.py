#!/usr/bin/python3

import string
import random

def encrypt(word, list_solved):
    """Создаем строку с визуально зашифрованным словом, с учетом отгаданных
    ранее букв. Здесь же 'инициализируется' список solved, наполняясь символами
    подчеркивания"""

    encrypted_word = ""
    if not list_solved:
        for ch in word:
            list_solved.append("_")
    for ch in list_solved:
        encrypted_word += ch + " "
    return encrypted_word

def letter_solved(letter, word, list_solved):
    """Ищет введенную букву в загаданном слове и если находит - \
    добавляет в список solved на соответствующую ей позицию"""
    for index in range(len(word)):
        if letter == word[index]:
            list_solved[index] = letter

def greeting_line(encrypted_word, state):
    """Динамически меняет строку приветствия, в зависимости от статуса \
    исполнения программы"""
    greeting = ""
    if state == "start":
        greeting = "Начинаем играть : "
    elif state == "success":
        greeting = "Есть такая буква! : "
    elif state == "failure":
        greeting = "Нет такой буквы! :"
    elif state == "repeat":
        greeting = "Такую букву уже называли! :"
    elif state == "error":
        greeting = "Ошибка ввода! :"
    print(greeting + encrypted_word)

def main():

    secret_list = ["python", "javascript", "basic", "pascal", "R"]
    secretword = secret_list[random.randrange(len(secret_list))]

    game_state = "start"

# Здесь - уже названные, но не отгаданные буквы
    guessed_letters = []

# Здесь - отгаданные буквы
    solved = []

# Это замена загаданного слова строкой из подчеркиваний
    encrypted = encrypt(secretword, solved)

    while True:

        greeting_line(encrypted, game_state)
        user_input = input("Введите букву: ")

        if not user_input or len(user_input) > 1 or user_input not in \
                string.ascii_letters or user_input in string.punctuation:
            game_state = "error"

        elif user_input in secretword and user_input not in solved:
            letter_solved(user_input, secretword, solved)
            encrypted = encrypt(secretword, solved)
            game_state = "success"

        elif user_input not in secretword:

            if user_input not in guessed_letters:
                guessed_letters.append(user_input)
                game_state = "failure"

            elif user_input in guessed_letters:
                game_state = "repeat"

        if "_" not in solved:
            break
    print("Поздравляем, вы отгадали слово! : " + encrypted)



if __name__ == '__main__':
    main()
