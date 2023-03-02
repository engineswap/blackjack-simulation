import random

class Card():
    def __init__(self, suit, id):
        self.suit = suit
        self.id = id
    
    def __str__(self):
        return self.suit + str(self.id)
    
    def getId(self):
        return self.id
    
    def getSuit(self):
        return self.suit

class Shoe():

    def __init__(self, numDecks):
        self.shoe = []
        suits = ["C", "H", "S", "D"]
        for i in range(numDecks):
            deck = [Card(suit, val) for suit in suits for val in range(1,14)]
            self.shoe += (deck)

    def __str__(self):
        cards = [str(card) for card in self.shoe]
        return "[" + ", ".join(cards) + "]"
    
    def shuffle(self):
        random.shuffle(self.shoe)

    def draw_1(self):
        return self.shoe.pop(0)

    def draw_n(self, count=1):
        res = self.shoe[:count]
        self.shoe = self.shoe[count:]
        return res

    def __len__(self):
        return len(self.shoe)
