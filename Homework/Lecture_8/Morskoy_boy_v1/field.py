

class Field():

    def __init__(self, x, y):
        self.isShip     = False
        self.isHit      = False
        self.isMiss     = False
        self.isAdjacent = False

    def __str__(self):
        if self.isHit:
            return 'X'
        elif self.isShip:
            return 'S'
        elif self.isMiss:
            return '*'
        else:
            return '.'
