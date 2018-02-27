
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
    total_ship_fields = 0

    for field in p1.ownboard:
        for ix in range(len(field)):
            if field[ix].isShip:
                total_ship_fields += 1
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

    if hit1 or hit2 == total_ship_fields:
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
        print('\n' * 1)

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
        print('\n' * 1)

    def placeShips(self):

        ship_type = [
                ('4 deck', 4, 1),
#                ('3 deck', 3, 2),
#                ('2 deck', 2, 3),
#                ('single deck', 1, 4),
        ]
        for ship in ship_type:

            ship_name = ship[0]
            num_of_ships = ship[2]
            prompt_ships_remaining = ship[2]
            ship_size = ship[1]

            i = 0
            while i < num_of_ships:

                clearScreen()
                self.showBoard()
                x, y = self.getPosition('start', ship_name, prompt_ships_remaining)
                ship_dir = self.getDirection(ship_size)

                try:
                    self.checkBounds(x, y, ship_size, ship_dir)
                    self.checkAdjacent(x, y, ship_size, ship_dir)
                except RuntimeError as e:
                    print(e)
                    sleep(2)
                    continue

                self.drawShip(x, y, ship_size, ship_dir)

                i += 1
                clearScreen()
                prompt_ships_remaining -= 1

        self.showBoard()
        sleep(3)

    def getPosition(self, mode, ship_name=None, prompt_ships_remaining=None):
        ship_pos = ''
        while not ship_pos:

            if mode == 'start':
                ship_pos = input('Enter starting coordinate for your {} ship (ex: a4, remaining ships: {}): '.format(ship_name, prompt_ships_remaining))
            elif mode == 'move':
                self.showBoard('enemy')
                ship_pos = input('Enter coordinates for your shot (ex: d5): ')

            extract_pos = re.search(r'(?:([a-jA-J])(10|[1-9]))', ship_pos)

            if not extract_pos or not ship_pos or len(ship_pos) < 2 \
                    or (len(ship_pos) == 3 and ship_pos[2] != '0'):
                print('Check your input!')
                sleep(1)
                ship_pos = ''
                clearScreen()
                continue
            else:
                x = COORD_LETTERS.get(extract_pos.group(1).upper())
                y = int(extract_pos.group(2)) - 1
                break
        return (x, y)

    def getDirection(self, ship_size):
        ship_dir = ''
        if ship_size == 1:
            return 'u'
        while not ship_dir:
            ship_dir = input('Enter direction of ship (u[p]|d[own]|l[eft]|r[ight]): ')
            if ship_dir not in ['u', 'd', 'l', 'r']:
                print('Check your input!')
                ship_dir = ''
                continue
            else:
                break
        return ship_dir

    def checkBounds(self, x, y, ship_size, ship_dir):
        pass
        for i in range(ship_size):
            if x < 0 or y < 0 or x > 9 or y > 9:
                raise RuntimeError('Ship out of bounds, retry!')
            elif ship_dir == 'd':
                    y += 1
            elif ship_dir == 'u':
                    y -= 1
            elif ship_dir == 'l':
                    x -= 1
            elif ship_dir == 'r':
                    x += 1

    def drawShip(self, x, y, ship_size, ship_dir):

        for i in range(ship_size):
            self.ownboard[x][y].isShip = True
            self.makeAdjacent(x, y)

            if ship_dir == 'd':
                    y += 1
            elif ship_dir == 'u':
                    y -= 1
            elif ship_dir == 'l':
                    x -= 1
            elif ship_dir == 'r':
                    x += 1

    def move(self, other):
        move_result = ''
        clearScreen()
        x, y = self.getPosition('move')

        if other.ownboard[x][y].isShip == True:
            other.ownboard[x][y].isHit = True
            self.enemyboard[x][y].isHit = True
            clearScreen()
            self.showBoard('enemy')
            print('HIT!')
            sleep(3)

        else:
            other.ownboard[x][y].isMiss = True
            self.enemyboard[x][y].isMiss = True
            clearScreen()
            self.showBoard('enemy')
            print('MISS!')
            sleep(3)
            move_result = 'miss'
            return move_result

    def checkAdjacent(self, x, y, ship_size, ship_dir):

        for i in range(ship_size):
            if self.ownboard[x][y].isAdjacent:
                raise RuntimeError('Ship adjacent to existing ship. Retry!')
            if ship_dir == 'd':
                    y += 1
            elif ship_dir == 'u':
                    y -= 1
            elif ship_dir == 'l':
                    x -= 1
            elif ship_dir == 'r':
                    x += 1

    def makeAdjacent(self, x, y):

        x_pos = [x, x - 1, x + 1]
        y_pos = [y, y - 1, y + 1]

        if x == 0 and y == 0:
            x_pos.pop(1)
            y_pos.pop(1)

        elif x == 9 and y == 9:
            x_pos.pop(2)
            y_pos.pop(2)

        elif x == 9 and y == 0:
            x_pos.pop(2)
            y_pos.pop(1)

        elif x == 0 and y == 9:
            x_pos.pop(1)
            y_pos.pop(2)

        elif x == 0:
            x_pos.pop(1)

        elif x == 9:
            x_pos.pop(2)

        elif y == 0:
            y_pos.pop(1)

        elif y == 9:
            y_pos.pop(2)

        for x in x_pos:
            for y in y_pos:
                try:
                    self.ownboard[x][y].isAdjacent = True
                except:
                    continue














