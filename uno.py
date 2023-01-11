#FPS UNO
#make a function that saves wins to a txt document and read data everytime the game starts (use the open() function)
#add a start menu with a name input and optional house rules
#cumburgah

import random

colors=['red','yellow','green','blue','wild']
types=['0','1','2','3','4','5','6','7','8','9','reverse','skip','draw two']
wilds=['normal','draw four']

class game():
    def __init__(self):
        self.firstTurn=None
        self.amountOfPlayers=None
        self.houseRules=None
        self.currentTurn=None
        self.highscores=None

class card():
    def __init__(self):
        self.color=None
        self.type=None

    def cardSelection(self):
        self.color=random.choice(colors)
        if self.color=="wild":
            self.type=random.choice(wilds)

#4 colors, 10 numbers + specials, 108 in total
class deck(card):
    def __init__(self):
        self.numberOfCards=108
        self.drawRule=None
        self.drawnCard=None
        self.topOfDiscards=None

    def firstAction(self):
        for i in range():
            for j in range():
                

    def drawFunction(self,hand):
        for i in range(0,self.drawRule):
            hand+=1
            if self.drawncard==self.topOfDiscards
            #fix this to be same color/number


class player():
    def __init__(self):
        self.hand=[list]
        self.name=None



class opponent():
    def __init__(self):
        self.hand=[list]
        self.name=None

def main():




main()
