#FPS UNO
#BUG means to work on this or fix something
#make a function that saves wins to a txt document and read data everytime the game starts (use the open() function)
#add a start menu with a name input and optional house rules

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

    def start(self):
        startlist=["1.start game /n","2.change drawrule /n",'3.toggle 7s switch hands /n']
        print("welcome to FPS UNO (FPS not included), please input your name")
        self.playername=input()
        print("type the number of your choice /n")
        for i in range (0,3):
            print(startlist[i])
        bobsmom=str(input())

        if "1" in bobsmom:
            "the game will now start"
        elif "2" in bobsmom:
            print("input your drawrule(input how many times you want to take a card from the deck if you don't have a card you can play) /n")
            deck.drawrule=int(input())
        elif "3" in bobsmom:
            print("when you play 7's they now allow you to switch hands with a player of your choice")


class card():
    def __init__(self):
        self.color=None
        self.type=None

    def cardSelection(self):
        self.color=random.choice(colors)
        if self.color=="wild":
            self.type=random.choice(wilds)
        else:
            self.type=random.choice(types)
        cardName=f"{self.color} {self.type}"

        return cardName

#4 colors, 10 numbers + specials, 108 in total
class deck():
    def __init__(self):
        self.numberOfCards=108
        self.drawrule=1
        self.drawnCard=None
        self.topdisc=None

    def firstDiscard(self):
        self.topdisc=card.cardSelection(card)
        print(f"The first card is {self.topdisc}")
    
    def draw_function(self):
        self.drawrule=1
        for i in range(0,self.drawrule):
            self.drawnCard=card.cardSelection(card)
            print(f"You draw a card, your card is {self.drawnCard}")
            
            tempCard=self.drawnCard.split(" ")
            tempCardTwo=self.topdisc.split(" ")
            if tempCard[0]=="wild":
                print(f"Your card is a wild, would you like to play it?")
                playChoice=input("y/n ")
                if playChoice=="y":
                    #BUG make this play card
                    return None
                else:
                    player.addToHand(self.drawnCard,player)
                break
            elif tempCard[0]==tempCardTwo[0] or tempCard[1]==tempCardTwo[1]:
                print(f"Your card matches the {self.topdisc} in the discards, would you like to play it?")
                playChoice=input("y/n ")
                if playChoice=="y":
                    #BUG make this play card
                    return None
                else:
                    player.addToHand(self.drawnCard,player)
                break


class player():
    def __init__(self):
        self.hand=[]
        self.name=None

    def startingHand(self):
        for i in range(0,7):
            self.hand.append(card.cardSelection(card))

    def addToHand(card,self):

        



class opponent():
    def __init__(self):
        self.hand=[]
        self.name=None

    def startingHand(self):
        for i in range(0,7):
            self.hand.append(card.cardSelection(card))

def main():
    uno=game()
    unoCard=card()
    unoDeck=deck()
    uno.start
    Player=player()
    Player.startingHand()
    

main()
#BUG add more functions and make the game work
