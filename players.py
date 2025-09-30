class Player(object):
    """ A player for a game. """
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.points = 0
        self.tricks = 0
        self.honors = 0

    def getName(self): 
        return self.name

    def resetPlayer(self):
        self.tricks = 0
        self.honors = 0

    def addTrick(self):
        self.tricks += 1

    def getTricks(self):
        return self.tricks

    def addHonors(self, numHonors):
        self.honors += numHonors

    def getHonors(self):
        return self.honors

    def addPoints(self, points):
        self.points += points

    def getPoints(self):
        return self.points

    def setHand(self, hand):
        self.hand = hand

    def getHand(self):
        return self.hand

    def addCard(self, card):
        self.hand.add(card)

    def removeCard(self, card):
        self.hand.remove(card)

    def __str__(self):
        return self.name + ":\t" + str(self.points)
