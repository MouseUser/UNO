#FPS UNO
#BUG means to work on this or fix something
#make a function that saves wins to a txt document and read data everytime the game starts (use the open() function)
#make a function to let the player play a card
#let the player choose what to do with inputs (draw, play [cardname])

import random

colors=['red','yellow','green','blue','wild']
types=['0','1','2','3','4','5','6','7','8','9','reverse','skip','draw two']
wilds=['normal','draw four']
aiNames=["HAL","Dave","ChatGPT","GLaDOS","Elvis","Bob","Jim","Rat","John"]
usedNames=[]
playerHand=[]
oppOneHand=[]
oppTwoHand=[]
oppThreeHand=[]
currentTurn=0
topdisc=[]

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
        self.amountOfPlayers=4

    def start(self):
        player.name=input("Welcome to UNO, please input your name: ")
        #begins the game
        print("The game will now start")
        player.startingHand(player)
        opponent.oppstartingHand(opponent)
        print("You draw your hand")
        print(playerHand)

    def turnOrder(self,current):
        if self.reverse is True:
            if currentTurn==4:
                currentTurn=0
        else:
            if currentTurn==-1:
                currentTurn=3
    
    def firstturn(self): #deprecated (actions already done in main gameplay)
        if "1" in self.firstTurn:
            action=input("it is your turn, type the card you would like to play, if you have no available cards, type draw")
            if "draw" in input:
                deck.draw_function()
        else:
            print("the AI are taking their turns, please wait ")

    def playCards(card,self,currentTurn): #BUG add more to reverse and draw two cards
        
        topdisc=card
        if currentTurn==0:
            playerHand.remove(card)
        elif currentTurn==1:
            oppOneHand.remove(card)
        elif currentTurn==2:
            oppTwoHand.remove(card)
        elif currentTurn==3:
            oppThreeHand.remove(card)

        if "skip" in card:
            if self.reverse is True:
                if currentTurn==0:
                    print("You have been skipped")
                else:
                    print(f"{playerList[currentTurn]} has been skipped")

                currentTurn-=2
            else:
                if currentTurn==0:
                    print("You have been skipped")
                else:
                    print(f"{playerList[currentTurn]} has been skipped")

                currentTurn+=2
            game.turnOrder(game)

            
        elif "reverse" in card:
            print("The turn order has been reversed")
            if self.reverse is True:
                self.reverse=False
                currentTurn+=1
            else:
                self.reverse=True
                currentTurn-=1
            game.turnOrder(game)
        elif "draw two" in card:
            if self.reverse==False:
                currentTurn+=1
            else:
                currentTurn-=1
            game.turnOrder(game)

            if currentTurn==0:
                print("You must draw two")
                newCards=[]
                for i in range(0,2):
                    deck.drawnCard=card.cardSelection(card)
                    newCards.append(deck.drawnCard)
                    playerHand.append(deck.drawnCard)
                print(f"You drew {newCards}")
            elif currentTurn==1:
                print(f"{playerList[currentTurn]} must draw two")
                for i in range(0,2):
                    deck.drawnCard=card.cardSelection(card)
                    oppOneHand.append(deck.drawnCard)
            elif currentTurn==2:
                print(f"{playerList[currentTurn]} must draw two")
                for i in range(0,2):
                    deck.drawnCard=card.cardSelection(card)
                    oppTwoHand.append(deck.drawnCard)
            elif currentTurn==3:
                print(f"{playerList[currentTurn]} must draw two")
                for i in range(0,2):
                    deck.drawnCard=card.cardSelection(card)
                    oppThreeHand.append(deck.drawnCard)
        
        elif card=="wild normal":
            if currentTurn==0:
                while True:
                    color=input("What color would you like to choose? ")
                    if color in colors:
                        break
            else:
                color=random.choice(colors)
            topdisc=f"{color} wild"
            print(f"The discard is now {topdisc}")
            
            if self.reverse is True:
                currentTurn-=1
            else:
                currentTurn+=1
            game.turnOrder(game)
        
        elif card=="wild draw four":
            if currentTurn==0:
                while True:
                    color=input("What color would you like to choose? ")
                    if color in colors:
                        break
            else:
                color=random.choice(colors)
            topdisc=f"{color} wild"
            print(f"The discard is now {topdisc}")
            

            if self.reverse is True:
                currentTurn-=1
            else:
                currentTurn+=1
            game.turnOrder(game)

            if currentTurn==0:
                print("You must draw four")
                newCards=[]
                for i in range(0,4):
                    deck.drawnCard=card.cardSelection(card)
                    newCards.append(deck.drawnCard)
                    playerHand.append(deck.drawnCard)
                print(f"You drew {newCards}")
            elif currentTurn==1:
                print(f"{playerList[currentTurn]} must draw four")
                for i in range(0,4):
                    deck.drawnCard=card.cardSelection(card)
                    oppOneHand.append(deck.drawnCard)
            elif currentTurn==2:
                print(f"{playerList[currentTurn]} must draw four")
                for i in range(0,4):
                    deck.drawnCard=card.cardSelection(card)
                    oppTwoHand.append(deck.drawnCard)
            elif currentTurn==3:
                print(f"{playerList[currentTurn]} must draw four")
                for i in range(0,4):
                    deck.drawnCard=card.cardSelection(card)
                    oppThreeHand.append(deck.drawnCard)

    def gameplayLoop(self):
        global playerList
        oppOne=opponent()
        oppTwo=opponent()
        oppThree=opponent()
        currentTurn=0
        topdisc=card.cardSelection(card)

        oppOne.nameSelection()
        oppTwo.nameSelection()
        oppThree.nameSelection()

        game.start()
        playerList=[player.name,oppOne.name,oppTwo.name,oppThree.name]
        print(f"The first card is {topdisc}")
        deck.firstCardAction(deck,currentTurn,topdisc)
        currentTurn,topdisc=deck.firstCardAction(deck,currentTurn,topdisc)
        while True:
            deck.checkForMatchingCard(topdisc)


                     



        


    






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

    def checkForMatchingCard(self,topdisc):
        availableCards=[]
        for i in range(0,len(playerHand)):
            tempCard=topdisc.split(" ")
            tempCardTwo=playerHand[i].split(" ")
            if tempCardTwo[0]=="wild" or tempCard[0]==tempCardTwo[0] or tempCard[1]==tempCardTwo[1]:
                availableCards.append(playerHand[i])
        if len(availableCards)>=1:
            gameInput=input(f"These {availableCards} match the discards, would you like to play one or draw? (play [card name]/draw) ")
            if "play" in gameInput.lower():
                tempVar=gameInput.lower().split("play ")
                if tempVar[1] in availableCards:
                    game.playCards(tempVar[1],game,currentTurn)
                else:
                    deck.checkForMatchingCard(deck)
            elif "draw" in gameInput.lower():
                deck.draw_function(deck)
            else:
                deck.checkForMatchingCard(deck)
        else:
            print("You do not have any matching cards, you must draw")
            deck.draw_function(deck)
    
    def firstCardAction(self,currentTurn,topdisc):
        if "skip" in topdisc:
            print("You have been skipped")
            currentTurn+=1
        elif "reverse" in topdisc:
            print("Turn order has been reversed")
            game.reverse=True
        elif "draw two" in topdisc:
            print("You must draw two")
            newCards=[]
            for i in range(0,2):
                newCards.append(card.cardSelection(card))
                playerHand.append(card.cardSelection(card))
            print(f"You drew {newCards}")
        elif topdisc=="wild normal":
            while True:
                    color=input("What color would you like to choose? ")
                    if color in colors:
                        break
            topdisc=f"{color} wild"
            print(f"The discard is now {topdisc}")
        elif topdisc=="wild draw four":
            while True:
                    color=input("What color would you like to choose? ")
                    if color in colors:
                        break
            topdisc=f"{color} wild"
            print(f"The discard is now {topdisc}")
            print("You must draw four")
            newCards=[]
            for i in range(0,4):
                deck.drawnCard=card.cardSelection(card)
                newCards.append(deck.drawnCard)
                playerHand.append(deck.drawnCard)
            print(f"You drew {newCards}")
            currentTurn+=1
        return currentTurn,topdisc

def main():
    global topdisc
    global playerList
    global playerHand
    global oppOneHand
    global oppTwoHand
    global oppThreeHand
    global currentTurn

    game.gameplayLoop()


main()
#BUG could add rules to main menu
#BUG wild cards need to have a set(random)color if they are first or played by npcs
#BUG in houserules: toggle 7s doesnt reflect current state of that houserule (still says enabled)
#BUG add more functions and make the game work
#guh
