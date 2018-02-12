#!/usr/bin/python

import random
import time
import string


def prettyPrint(func):

    def inner(*args):
        print("-" * 28)
        func(*args)
        print()
        print("-" * 28)
    return inner


class Hand():

    def __init__(self, name, cards_needed=2):
        self.hand = list()
        self.buffer = list()
        self.name = name
        self.cards_needed = cards_needed


    @prettyPrint
    def show_hand(self, hand_or_buffer="hand"):
        cnt = 1
        print("{}:".format(self.name))

        if hand_or_buffer == "hand":
            hand = self.hand

        if hand_or_buffer == "buffer":
            hand = self.buffer

        for card in hand:
            print("*{}*:".format(cnt), card, end="  |  ")
            cnt += 1


    def move(self, table):
        """Позволяет сформировать у игрока отдельную "руку" с комбинацией
        карт, из своих и тех, что на столе (для удобства сравнения с
        оппонентом). Сортирует карты в этой отдельной "руке" по параметру
        value карты"""

        selection = input("\nSelect cards from your deck: ")
        for index in selection:
            self.buffer.append(self.hand[int(index) - 1])

        selection = input("\nSelect cards from the table: ")
        for index in selection:
            self.buffer.append(table.hand[int(index) - 1])

        self.buffer = sorted(self.buffer, key=lambda card: card.value)


class Table(Hand):

    def turn(self, deck):
        self.cards_needed += 1
        deck.deal(self)

    def river(self, deck):
        self.cards_needed += 1
        deck.deal(self)


class Card():

    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    def __repr__(self):
        return repr((self.name, self.suit, self.value))

    def __str__(self):
        return "({} {})".format(self.name, self.suit)


class CardPack():

    suits = [

            "♠",
            "♣",
            "♦",
            "♥",

        ]

    cards = {

            2 : "2",
            3 : "3",
            4 : "4",
            5 : "5",
            6 : "6",
            7 : "7",
            8 : "8",
            9 : "9",
            10 : "10",
            11 : "J",
            12 : "Q",
            13 : "K",
            14 : "A",

        }

    def __init__(self):

        self.pack = list()

        for suit in CardPack.suits:

            for value, name in CardPack.cards.items():
                self.pack.append(Card(name, suit, value))

        print('\nShuffling... Deck currently contains {} cards'.format(len(self.pack)))
        random.shuffle(self.pack)
        time.sleep(1)


    def deal(self, *args):
        players = [*args]
        for player in players:
            print("\nDealing {} card(s) --> {}...".format(player.cards_needed, player.name))
            for i in range(player.cards_needed):
                dealt = self.pack.pop()
                player.hand.append(dealt)
                player.cards_needed = 0
            time.sleep(1)


def main():

    deck = CardPack()

    player1 = input("Enter your name, player1: ")
    player1 = Hand(player1)

    player2 = input("Enter your name, player2: ")
    player2 = Hand(player2)

    table_cards = Table('Table', 3)

    deck.deal(player1, player2, table_cards)

    print("\n\nFLOP\n\n")
    table_cards.show_hand()
    player1.show_hand()
    player2.show_hand()
    input("Press any key to continue")

    table_cards.turn(deck)

    print("\n\nTURN\n\n")
    table_cards.show_hand()
    player1.show_hand()
    player2.show_hand()
    input("Press any key to continue")

    table_cards.river(deck)

    print("\n\nRIVER\n\n")
    table_cards.show_hand()
    player1.show_hand()
    player1.move(table_cards)

    table_cards.show_hand()
    player2.show_hand()
    player2.move(table_cards)

    player1.show_hand("buffer")
    player2.show_hand("buffer")

    input("Press any key to exit")


if __name__ == '__main__':
    main()
