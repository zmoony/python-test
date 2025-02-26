import random
from enum import Enum

class Suite(Enum):
    """花色枚举"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

class Card:
    """牌"""
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        """
        类似于toString()
        :return:
        """
        suites = ['♠', '♥', '♣', '♦']
        faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]} {faces[self.face]}'

class Poker:
    """扑克"""

    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite for face in range(13)]
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return self.current < len(self.cards)

class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def sort(self):
        """排序"""
        self.cards.sort(key=lambda x: (x.suite.value, x.face))


if __name__ == '__main__':
    poker = Poker()
    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get_one(poker.deal())
    for player in players:
        player.sort()
        print(player.name, player.cards)

