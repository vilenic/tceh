#!/usr/bin/python

import random


class Hand():

    def __init__(self, name, count=5):
        self.hand = list()
        self.name = name
        self.count = count

    def show_hand(self):
        cnt = 1
        print()
        print("{}'s current hand:".format(self.name))
        for index in range(len(self.hand)):
            print("{}: {}".format(cnt, self.hand[index]))
            cnt += 1


class Card():

    def __init__(self, value, suit, inhand=False):
        self.value = value
        self.suit = suit
        self.inhand = inhand

    def __repr__(self):
        return "{} of {} (Currently in hand: {})".format(self.value, self.suit, self.inhand)

    suits = [
            "spades",
            "clubs",
            "diamonds",
            "hearts",
        ]

    plain_cards = [
            "6",
            "7",
            "8",
            "9",
            "10",

        ]

    title_cards = [
            "Jack",
            "Dame",
            "King",
            "Ace",
        ]


class CardPack():

    def __init__(self):

        self.pack = list()

        for suit in Card.suits:

            for card in Card.plain_cards:
                self.pack.append(Card(card, suit))

            for card in Card.title_cards:
                self.pack.append(Card(card, suit))

    def show(self):
        cnt = 1
        print()
        print("Current deck:")
        for index in range(len(self.pack)):
            print("{}: {}".format(cnt, self.pack[index]))
            cnt += 1

    def shuffle(self):
        print('\nShuffling... Deck currently contains {} cards'.format(len(self.pack)))
        random.shuffle(self.pack)

    def deal(self, player):
        print("\nDealing {} cards to {}'s hand...".format(player.count, player.name))
        for i in range(player.count):
            dealt = self.pack.pop()
            dealt.inhand = True
            player.hand.append(dealt)

player1 = Hand("Ivan")

deck = CardPack()

deck.shuffle()

deck.deal(player1)

player1.show_hand()
