
import re
import os
import string
from field import Field
from time import sleep

COORD_LETTERS = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7,
    'I' : 8,
    'J' : 9,
}

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def win_condition(p1, p2):
    hit1 = 0
    hit2 = 0
    total_fields = 0

    for field in p1.ownboard:
        for ix in range(len(field)):
            if field[ix].isShip:
                total_fields += 1
            elif field[ix].isHit:
                hit1 += 1
            else:
                continue

    for field in p2.ownboard:
        for ix in range(len(field)):
            if field[ix].isHit:
                hit2 += 1
            else:
                continue

    if hit1 or hit2 == total_fields:
        return True

class Seabattle():

    def __init__(self, name):
        self.ownboard = []
        self.enemyboard = []
        self.name = name
        self.makeBoards()

    def makeOwnBoard(self):
        for i in range(10):
            self.ownboard.append([])
            for j in range(10):
                self.ownboard[i].append(Field(i, j))

    def makeEnemyBoard(self):
        for i in range(10):
            self.enemyboard.append([])
            for j in range(10):
                self.enemyboard[i].append(Field(i, j))

    def showBoards(self):

        self.showBoard()
        self.showBoard('enemy')

    def makeBoards(self):

        self.makeOwnBoard()
        self.makeEnemyBoard()

    def showBoard(self, which='own'):

        print('\n' * 1)
        print('*' * (len(self.name) + 4))
        print('*', self.name, '*')
        print('*' * (len(self.name) + 4))
        print('\n' * 2)

        if which == 'own':
            board = self.ownboard
            print('Your board:')
        elif which == 'enemy':
            board = self.enemyboard
            print('Enemy board:')

        print('-' * 22)

        print('   ', end='')

        top_coord_row = COORD_LETTERS.keys()

        for letter in top_coord_row:
            print(letter, end = ' ')
        print()

        left_coord_row = [i for i in range(9)]

        for number in left_coord_row:
            print(number + 1, end='  ')
            for i in range(10):
                print(board[i][number], end=' ')
            print()
        print('10', end=' ')
        for j in range(10):
            print(board[j][9], end=' ')
        print()

        print('-' * 22)
        print('\n' * 2)

    def placeShips(self):

        ship_type = [
                ('4 deck', 4, 1),
#                ('3 deck', 3, 2),
#                ('2 deck', 2, 3),
#                ('single deck', 1, 4),
        ]
        clearScreen()
        for ship in ship_type:
            ship_name = ship[0]
            num_of_ships = ship[2]
            remaining = ship[2]
            size_of_ship = ship[1]

            for i in range(num_of_ships):
                self.showBoard()
                x, y = self.getPosition('start', ship_name, remaining)
                ship_dir = self.getDirection()
                self.drawShip(x, y, size_of_ship, num_of_ships, ship_dir)
                clearScreen()
            remaining -= 1
        self.showBoard()
        sleep(2)

    def getPosition(self, mode, ship_size=None, remaining=None):
        ship_pos = ''
        while not ship_pos:

            if mode == 'start':
                ship_pos = input('Enter starting coordinate for your {} ship (ex: a4, remaining ships: {}): '.format(ship_size, remaining))
            elif mode == 'move':
                ship_pos = input('Enter coordinates for your shot (ex: d5): ')
                for ch in ship_pos:
                    if ch in string.punctuation or string.whitespace:
                        continue

            extract_pos = re.search(r'(?:([a-jA-J])(10|[1-9]))', ship_pos)
            if not extract_pos or len(ship_pos) < 2:
                print('Check your input!')
                ship_pos = ''
                continue
            else:
                x = COORD_LETTERS.get(extract_pos.group(1).upper())
                y = int(extract_pos.group(2)) - 1
                break
        return (x, y)

    def getDirection(self):
        ship_dir = ''
        while not ship_dir:
            ship_dir = input('Enter direction of ship (u[p]|d[own]|l[eft]|r[ight]): ')
            if ship_dir not in ['u', 'd', 'l', 'r']:
                print('Check your input!')
                ship_dir = ''
                continue
            else:
                break
        return ship_dir

    def drawShip(self, x, y, size, num, ship_dir):
            if ship_dir == 'd':
                for i in range(size):
                    self.ownboard[x][y].isShip = True
                    y += 1
            if ship_dir == 'u':
                for i in range(size):
                    self.ownboard[x][y].isShip = True
                    y -= 1
            if ship_dir == 'l':
                for i in range(size):
                    self.ownboard[x][y].isShip = True
                    x -= 1
            if ship_dir == 'r':
                for i in range(size):
                    self.ownboard[x][y].isShip = True
                    x += 1

    def move(self, other):
        move_result = ''
        clearScreen()
        self.showBoard('enemy')
        x, y = self.getPosition('move')

        if other.ownboard[x][y].isShip == True:
            other.ownboard[x][y].isHit = True
            self.enemyboard[x][y].isHit = True
            clearScreen()
            self.showBoard('enemy')
            sleep(1)

        else:
            other.ownboard[x][y].isMiss = True
            self.enemyboard[x][y].isMiss = True
            clearScreen()
            self.showBoard('enemy')
            sleep(1)
            move_result = 'miss'
            return move_result

