#!/usr/bin/python3

import random

def drawTable(table):
    """Отрисовывает игровое поле, используя вложенные списки в качестве
    рядов"""

    for i in range(4):
        print('-' * 20)
        print(end="| ")

        for index in range(4):
            print(table[i][index], end=" | ")

        print()

    print('-' * 20)


def getPosition(table):
    """Устанавливает текущее положение пустого поля в списке и возвращает его
    в кортеже"""

    for i in range(4):
        try:
            pos = table[i].index(" ")
            return i, pos
        except:
            pass

def checkInput(string):
    """Проверка пользовательского ввода"""
    if string not in "udlr":
        return False
    return True

def checkMove(move, current):
    """Проверка недопустимости заданного пользователем хода (крайние положения
    игрового поля). Возвращает True, если ход возможен"""

    if current[0] == 0 and move == "u" or current[0] == 3 and move == "d":
        return False
    if current[1] == 0 and move == "l" or current[1] == 3 and move == "r":
        return False
    return True


def makeMove(direction, board):
    """Осуществление хода. Ищет пустое поле и осуществляет взаимную замену
    значений либо внутри вложенного списка, либо между соседними на основе
    индексов"""

    pos = getPosition(board)
    check = checkMove(direction, pos)

    if not check:
        raise RuntimeError('Запрошен некорректный ход')

    cursor = board[pos[0]].pop(pos[1])

    if direction == "u":
        previousValue = board[pos[0] - 1].pop(pos[1])
        board[pos[0] - 1].insert(pos[1], cursor)
        board[pos[0]].insert(pos[1], previousValue)

    if direction == "d":
        previousValue = board[pos[0] + 1].pop(pos[1])
        board[pos[0] + 1].insert(pos[1], cursor)
        board[pos[0]].insert(pos[1], previousValue)

    if direction == "l":
        board[pos[0]].insert(pos[1] - 1, cursor)

    if direction == "r":
        board[pos[0]].insert(pos[1] + 1, cursor)


def init():
    """Создает поле на основе списка, наполненного значениями от 1 до 15 +
    строка из пробела. Бъет его на вложенные списки из 4 элементов"""

    def split(biglist):

        newlist = []
        a, b = (0, 4)

        for i in range(4):
            newlist.append(biglist[a:b])
            a += 4
            b += 4

        return newlist

    biglist = []

    for n in range(1, 16):
        biglist.append(n)

    biglist.append(" ")
    random.shuffle(biglist)

    biglist = split(biglist)

    return biglist

def prompt():
    """Строка справки"""

    print("\nХодим пустым полем.\nu - вверх, d - вниз, l - влево, r - вправо\n")

def main():

    success_state = [

            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, " "]

    ]

    gameboard = init()
    prompt()
    try:

        while gameboard != success_state:

            drawTable(gameboard)
            move = input("Ваш ход (? для справки): ")

            if move == "?":
                prompt()
                continue

            if checkInput(move):
                try:
                    makeMove(move, gameboard)
                except RuntimeError as e:
                    print(e)
                    print("Пробуем еще раз")
                    continue
            else:
                print("Проверяем корректность ввода!")
                continue

    except KeyboardInterrupt:
        print("\nДо свидания!")
        exit(0)

    print("Поздравлем! Вы решили головоломку!")

if __name__ == '__main__':
    main()
