# Cards Module
# Basic classes for a game with playing cards

class Card(object):
    """ A playing card. """
    RANKS = ["A", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def flip(self):
        self.is_face_up = not self.is_face_up

    def equal(self, card2):
        if(self.rank==card2.rank and self.suit==card2.suit):
            return True
        else:
            return False
      
class Hand(object):
    """ A hand of playing cards. """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def remove(self, card):
        index = self.cardIndex(card)
        self.cards.pop(index)

    def cardIndex(self, card):
        for i in range(len(self.cards)):
            if(Card.equal(self.cards[i], card)):
                return i
        else:
            return -1
    
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def getLength(self):
        return len(self.cards)

class Deck(Hand):
    """ A deck of playing cards. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue deal. Out of cards!")



if __name__ == "__main__":
    input("\n\nPress the enter key to exit.")
    

