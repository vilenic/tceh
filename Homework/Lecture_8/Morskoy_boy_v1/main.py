#!/usr/bin/python3

import string
import os
from time import sleep
from seabattle import Seabattle, win_condition, clearScreen

if __name__ == '__main__':

    clearScreen()
    player1 = Seabattle('Player 1')
    player2 = Seabattle('Player 2')
    try:
        player1.placeShips()
        player2.placeShips()

        while True:

            while True:
                move_result = player1.move(player2)
                if move_result == 'miss':
                    break
                elif win_condition(player1, player2):
                    print('Congrats! You have won the game!')
                    exit(0)

            while True:
                move_result = player2.move(player1)
                if move_result == 'miss':
                    break
                elif win_condition(player1, player2):
                    print('Congrats! You have won the game!')
                    exit(0)
    except KeyboardInterrupt:
        print()
        print("GG WP BB!")
        sleep(1)
        exit(0)
