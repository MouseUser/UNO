#FPS UNO
#BUG means to work on this or fix something
#make a function that saves wins to a txt document and read data everytime the game starts (use the open() function)
#make a function to let the player play a card
#let the player choose what to do with inputs (draw, play [cardname])

import random

colors=['red','yellow','green','blue','wild']
types=['0','1','2','3','4','5','6','7','8','9','reverse','skip','draw two']
wilds=['normal','draw four']

aiNames=["HAL","Dave","ChatGPT","GLaDOS","Elvis Impostor","Bob","Jim","Rat"]

class game():
    def __init__(self):
        self.firstTurn=None
        self.houseRules=None
        self.currentTurn=None
        self.amountOfPlayers=4
        self.highscores=None
        self.playerList=[]
        self.reverse=False

    def start(self):
        startlist="1.Start Game","2.Edit House Rules","3.View Highscores"
 
        player.name=input("welcome to FPS UNO (FPS not included), please input your name:")
        while self.gamestart==False:
            print("type the number of your choice ")
            for i in range (0,3):
                print(startlist[i])
            userinput=str(input())
 
            if "1" in userinput:
                print("the game will now start")
                self.gamestart=True
            elif "2" in userinput:
                seconduserinput=input("1.edit drawrule 2.toggle 7s switch hands")
 
                if "1" in seconduserinput:
                    print("input your drawrule(input how many times you want to take a card from the deck if you don't have a card you can play) \n")
                    deck.drawrule=int(input())
                elif "2" in seconduserinput:
                    print("Number 7 cards now allow you to switch hands with a player of your choice")
                    self.houseRules=True
 
            elif "3" in userinput:
                print("FIX THIS WHEN YOU MAKE THE CODE THAT READS THE FILE") #BUG

    def begin_game():
        print("you draw your hand")
        print(player.hand) #BUG
    def firstPlayer(oppOne,oppTwo,oppThree,self):
        self.playerList=[player.name,oppOne.name,oppTwo.name,oppThree.name]
        self.firstTurn=random.randint(1,4)



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
    
    def draw_function(self): #BUG make this hook into the play card function so you can play cards if you draw
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

    def playCards(card,self): #BUG add more to reverse and draw two cards
        self.topdisc=card
        if "skip" in card:
            self.currentTurn+=2
        elif "reverse" in card:
            self.currentTurn-=1
            game.reverse=True
            #make this count backward for turns
        elif "draw two" in card:
            if game.reverse==False:
                self.currentTurn+=1
            else:
                self.currentTurn-=1
            for i in range(0,len(game.playerList)):
                #make the next player draw two cards and skip their turn

class player():
    def __init__(self):
        self.hand=[]
        self.name=None

    def startingHand(self):
        for i in range(0,7):
            self.hand.append(card.cardSelection(card))

    def addToHand(card,self):
        self.hand.append(card)
        
class opponent():
    def __init__(self):
        self.hand=[]
        self.name=random.choice(aiNames)

    def startingHand(self):
        for i in range(0,7): 
            self.hand.append(card.cardSelection(card))

def main():
    uno=game()
    unoCard=card()
    unoDeck=deck()
    Player=player()
    oppOne=opponent()
    oppTwo=opponent()
    oppThree=opponent()
    uno.start()
    Player.startingHand()
    #make the game do the stuff in order
    

main()
#BUG add more functions and make the game work
#guh
