from cards import Card
from cards import Deck
from cards import Hand
from players import Player

numPlayers = int(input("Number of players: "))
players = []

for i in range(numPlayers):
    name = input("Name of Player " + str(i+1) + ":  ")
    players.append(Player(name))

numCards = 0
if(numPlayers==2): 
    numCards = 6
elif(numPlayers==4):
    numCards = 5
else:
    numCards = 3

def prepareDeck(): 
    deck1 = Deck()
    deck1.populate()
    deck1.shuffle()
    return deck1

def prepareHands(deck1):
    hands = []
    for i in range(len(players)):
        hands.append(Hand())
    deck1.deal(hands, per_hand = numCards)

    for i in range(len(players)):
        players[i].resetPlayer()
        players[i].setHand(hands[i])
        
def findHighest(cards):
    for i in range(0, len(cards)):
        if(cards[i][0]=='A'):
            cards[i] = "14" + cards[i][-1]
        elif(cards[i][0]=='K'):
            cards[i] = "13" + cards[i][-1]
        elif(cards[i][0]=='Q'):
            cards[i] = "12" + cards[i][-1]
        elif(cards[i][0]=='J'):
            cards[i] = "11" + cards[i][-1]
            
    suit = cards[0][-1]
    highestVal = int(cards[0][:-1])
    winner = 0
    for i in range(1, len(cards)):
        if(cards[i][-1]==suit and int(cards[i][:-1])>highestVal): 
            highestVal = int(cards[i][:-1])
            winner = i
    for i in range(0, len(cards)):        
        if(cards[i][-1]==suit and int(cards[i][:-1])==7 and highestVal==14):
            highestVal = 15
            winner = i
    return winner

def countHonors(cards):
    numHonors = 0
    for c in cards:
        if(c[:-1]=="A" or c[:-1]=="K" or c[:-1]=="Q" or c[:-1]=="J" or c[:-1]=="10"): 
            numHonors+=1
    return numHonors

def twentyHonors(players):
    winner = -1
    for i in range(0, len(players)):
        if(players[i].getHonors()>=20):
            winner = i
    return winner

def findWinner(players):
    highestVal = 0
    winner = 0
    for i in range(0, len(players)):
        if(players[i].getPoints()>highestVal):
            highestVal = players[i].getPoints()
            winner = i
    return winner

def printHands(players):
    print("\nThe current hands are: ")
    for p in players:
        print(p.getName(), ": \t", p.getHand())
    print("\n")

games = 0
winner = -1
finished = False

while(not finished):
    deck = prepareDeck()
    prepareHands(deck)

    startingPlayer = 0
    for i in range(int(32/numPlayers)):
        printHands(players)
        cardsPlaced = []
        for j in range(numPlayers):
            playerNum = startingPlayer + j
            if(playerNum>=numPlayers):
                playerNum -= numPlayers
                
            cardString = input(players[playerNum].getName() + " places card ")
            while(players[playerNum].getHand().cardIndex(Card(cardString[:-1],cardString[-1]))==-1):
                cardString = input("Please place a card in your hand: ")
            card = Card(cardString[:-1],cardString[-1])
                  
            players[playerNum].removeCard(card)
            cardsPlaced.append(cardString)

        tempHand = []
        tempHand.append(Hand())
        if(deck.getLength()>0):
            deck.deal(tempHand, per_hand = numPlayers)
            for k in range(numPlayers):
                players[k].addCard(tempHand[0].cards[k])

        numHonors = countHonors(cardsPlaced)
        roundWinner = findHighest(cardsPlaced) + startingPlayer
        if(roundWinner>=numPlayers):
            roundWinner -= numPlayers
        startingPlayer = roundWinner
        players[roundWinner].addHonors(numHonors)
        players[roundWinner].addTrick()

        print("\nRound winner: ", players[roundWinner].getName())
        print("\nCurrent stats: ")
        for p in players:
            print(p.getName(), ":    \t", p.getHonors(), " honors and\t", p.getTricks(), "Tricks")
        
        winner = twentyHonors(players)
        if(winner>=0):
            finished = True
            break

    for p in players:
        numHonors = p.getHonors()
        if(numHonors > 10):
             p.addPoints(p.getTricks())
        if(numHonors > 15):
             p.addPoints(p.getTricks())
        if(p.getPoints() > 100): 
            finished = True

    for p in players:
        print(p.getName(), ":\tPoints-", p.getPoints())

    games+=1
    if(games>2):
        finished = True

if(winner==-1): 
    winner = findWinner(players)
    print(players[winner].getName(), " wins with ", int(players[winner].getPoints()), " points!")
else:
    print(players[winner].getName(), " wins with ", int(players[winner].getHonors()), " honors!")
