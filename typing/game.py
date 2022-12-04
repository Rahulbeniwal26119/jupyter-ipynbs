from __future__ import annotations
import random
import sys

class Card:
    SUITS = "♠ ♡ ♢ ♣".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.suit}{self.rank}"


class Deck:
    def __init__(self, cards):
        self.cards = cards

    @classmethod
    def create(cls, shuffle=False) -> Deck:
        cards = [Card(s, r) for r in Card.RANKS for s in Card.SUITS]
        if shuffle:
            random.shuffle(cards)
        return cls(cards)

