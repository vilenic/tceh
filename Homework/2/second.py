#!/usr/bin/python3

from operator import itemgetter
import string

def strip_punctuation(text):
    """Убирает знаки препинания из строки. Добавляет пробел в конец новой
    строки для упрощения обработки в функции подсчета слов"""
    new_text = ""
    for ch in text.lower():
        if ch not in string.punctuation and ch not in string.digits:
            new_text += ch
        else:
            continue
    new_text += " "
    print('\nProcessed {} characters in supplied string'.format(len(text)))
    return new_text

def count_words(text):
    words = {}
    separate_word = ""
    for ch in text:
        if ch in string.whitespace:
            if separate_word == "":
                continue
            elif separate_word not in words.keys():
                words[separate_word] = 1
            else:
                words[separate_word] += 1
            separate_word = ""
        else:
            separate_word += ch
    print('Processed {} words in supplied string'.format(len(words)))
    return words

def top10(dictionary):
    """Берет словарь и преобразует его в сортированный (в обратном порядке,
    по второму значению в элементе списка) список с выводом первых 10
    индексов или соответствующего количества индексов"""
    list_of_counted = []
    for k, v in dictionary.items():
        list_of_counted.append((k, v))

    list_of_counted = sorted(list_of_counted, key=itemgetter(1), reverse=True)
    length = len(dictionary)
    if length >= 10:
        for i in range(10):
            print(list_of_counted[i][0], list_of_counted[i][1])
    else:
        for i in range(length):
            print(list_of_counted[i][0], list_of_counted[i][1])

#s = input("Дайте текст!\n\n")
s = """Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"""

stripped = strip_punctuation(s)
counted = count_words(stripped)
print("\nТекст: ", s)
print("\nСписок из ТОП-10 (часто встречающихся) слов в тексте:")
top10(counted)
