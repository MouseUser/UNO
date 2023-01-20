#FPS UNO
#BUG means to work on this or fix something
#make a function that saves wins to a txt document and read data everytime the game starts (use the open() function)
#make a function to let the player play a card
#let the player choose what to do with inputs (draw, play [cardname])

import random

global topdisc
global playerList
global playerHand
global oppOneHand
global oppTwoHand
global oppThreeHand

colors=['red','yellow','green','blue','wild']
types=['0','1','2','3','4','5','6','7','8','9','reverse','skip','draw two']
wilds=['normal','draw four']
aiNames=["HAL","Dave","ChatGPT","GLaDOS","Elvis","Bob","Jim","Rat","John"]
usedNames=[]
playerHand=[]
oppOneHand=[]
oppTwoHand=[]
oppThreeHand=[]


class player():
    def __init__(self):
        self.name=None

    def startingHand(self):
        for i in range(0,7):
            playerHand.append(card.cardSelection(card))

class opponent():
    def __init__(self):
        self.name=None

    def oppstartingHand(self):
        for i in range(0,7):
            oppOneHand.append(card.cardSelection(card))
            oppTwoHand.append(card.cardSelection(card))
            oppThreeHand.append(card.cardSelection(card))
    
    def nameSelection(self):
        while True:
            oppName=f"Bot {random.choice(aiNames)}"
            if oppName not in usedNames:
                usedNames.append(oppName)
                self.name=oppName
                break
        

class game():
    def __init__(self):
        self.currentTurn=0
        self.amountOfPlayers=4
        self.reverse=False

    def start(self):
        player.name=input("Welcome to UNO, please input your name: ")
        #begins the game
        print("The game will now start")
        player.startingHand(player)
        opponent.oppstartingHand(opponent)
        print("You draw your hand")
        print(playerHand)

    def turnOrder(self):
        if self.reverse is True:
            if self.currentTurn==4:
                self.currentTurn=0
        else:
            if self.currentTurn==-1:
                self.currentTurn=3
    
    def firstturn(self): #deprecated (actions already done in main gameplay)
        if "1" in self.firstTurn:
            action=input("it is your turn, type the card you would like to play, if you have no available cards, type draw")
            if "draw" in input:
                deck.draw_function()
        else:
            print("the AI are taking their turns, please wait ")

    def playCards(card,self): #BUG add more to reverse and draw two cards
        topdisc=card
        if self.currentTurn==0:
            playerHand.remove(card)
        elif self.currentTurn==1:
            oppOneHand.remove(card)
        elif self.currentTurn==2:
            oppTwoHand.remove(card)
        elif self.currentTurn==3:
            oppThreeHand.remove(card)

        if "skip" in card:
            if self.reverse is True:
                self.currentTurn-=2
            else:
                self.currentTurn+=2
            game.turnOrder(game)

            if self.currentTurn==0:
                print("You have been skipped")
            else:
                print(f"{playerList[self.currentTurn]} has been skipped")
        elif "reverse" in card:
            print("The turn order has been reversed")
            if self.reverse is True:
                self.reverse=False
                self.currentTurn+=1
            else:
                self.reverse=True
                self.currentTurn-=1
            game.turnOrder(game)
        elif "draw two" in card:
            if self.reverse==False:
                self.currentTurn+=1
            else:
                self.currentTurn-=1
            game.turnOrder(game)

            if self.currentTurn==0:
                print("You must draw two")
                newCards=[]
                for i in range(0,2):
                    deck.drawnCard=card.cardSelection(card)
                    newCards.append(deck.drawnCard)
                    playerHand.append(deck.drawnCard)
                print(f"You drew {newCards}")
            elif self.currentTurn==1:
                print(f"")


    






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
        self.drawnCard=None

    def draw_function(self): #BUG make this hook into the play card function so you can play cards if you draw
                self.drawnCard=card.cardSelection(card)
                print(f"You draw a card, your card is {self.drawnCard}")
                
                tempCard=self.drawnCard.split(" ")
                tempCardTwo=topdisc.split(" ")
                
                if tempCard[0]=="wild":
                    print(f"Your card is a wild, would you like to play it?")
                    playChoice=input("y/n ")
                    if playChoice=="y":
                        game.playCards(self.drawnCard)
                    else:
                        playerHand.append(self.drawnCard)
                elif tempCard[0]==tempCardTwo[0] or tempCard[1]==tempCardTwo[1]:
                    print(f"Your card matches the {topdisc} in the discards, would you like to play it?")
                    playChoice=input("y/n ")
                    if playChoice=="y":
                        game.playCards(self.drawnCard)
                    else:
                        playerHand.append(self.drawnCard)

    def checkForMatchingCard(self): #BUG finish this
        availableCards=[]
        for i in range(0,len(playerHand)):
            tempCard=topdisc.split(" ")
            tempCardTwo=player.Hand[i].split(" ")
            if tempCardTwo[0]=="wild" or tempCard[0]==tempCardTwo[0] or tempCard[1]==tempCardTwo[1]:
                availableCards.append(playerHand[i])
        if len(availableCards)>=1:
            gameInput=input(f"These {availableCards} match the discards, would you like to play one or draw? (play [card name]/draw) ")
            if "play" in gameInput.lower():
                tempVar=gameInput.lower().split("play ")
                if tempVar[1] in availableCards:
                    game.playCards(tempVar[1],game)
                else:
                    deck.checkForMatchingCard(deck)
            elif "draw" in gameInput.lower():
                deck.draw_function(deck)
            else:
                deck.checkForMatchingCard(deck)
        else:
            print("You do not have any matching cards, you must draw")
            deck.draw_function(deck)
    
    def firstCardAction(self):


def main():
    uno=game()
    unoCard=card()
    unoDeck=deck()
    Player=player()
    oppOne=opponent()
    oppTwo=opponent()
    oppThree=opponent()

    topdisc=card.cardSelection(card)

    
    oppOne.nameSelection()
    oppTwo.nameSelection()
    oppThree.nameSelection()

    



    uno.start()
    playerList=[player.name,oppOne.name,oppTwo.name,oppThree.name]
    print(f"The first card is {topdisc}")
    game.playCards(topdisc)
    unoDeck.checkForMatchingCard()



    #gameplay loop
    #while True:

        #make the game determine whos turn it is and 
    #make the game do the stuff in order

main()
#BUG could add rules to main menu
#BUG wild cards need to have a set(random)color if they are first or played by npcs
#BUG in houserules: toggle 7s doesnt reflect current state of that houserule (still says enabled)
#BUG add more functions and make the game work
#guh
