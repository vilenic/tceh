#!/usr/bin/python3

import string

def encrypt(word, guessed):
    encrypted_word = ""
    if guessed == []:
        for ch in word:
            encrypted_word += "_ "

    return encrypted_word

def check_guessed(word, guessed):
 
    pass




secretword = "python"


guessed_letters = []

while True:
    encrypted = encrypt(secretword, guessed_letters)
    user_input = input("Отгадайте слово: " + encrypted)
    if user_input in guessed_letters:
        print("Эту букву ({}) вы уже вводили! Пробуем еще раз.".format(user_input))
        continue
    elif user_input in secretword:
        print("Вы отгадали букву!")
        guessed_letters.append(user_input)
        continue
    elif user_input in string.whitespace:
        continue
    guessed_letters.append(user_input)
    print(guessed_letters)
