#FPS UNO
#BUG means to work on this or fix something
#make a function that saves wins to a txt document and read data everytime the game starts (use the open() function)
#make a function to let the player play a card
#let the player choose what to do with inputs (draw, play [cardname])

import random

colors=['red','yellow','green','blue','wild']
types=['0','1','2','3','4','5','6','7','8','9','reverse','skip','draw two']
wilds=['normal','draw four']
aiNames=["HAL","Dave","ChatGPT","GLaDOS","Elvis","Bob","Jim","Rat"]

class player():
    def __init__(self):
        self.hand=[]
        self.name=None

    def startingHand(self):
        self.hand=[]
        for i in range(0,7):
            self.hand.append(card.cardSelection(card))

    def addToHand(card,self):
        self.hand.append(card)

class opponent():
    def __init__(self):
        self.hand=[]
        self.name=random.choice(aiNames)

    def oppstartingHand(self):
        self.hand=[]
        for i in range(0,7):
            self.hand.append(card.cardSelection(card))

class game():
    def __init__(self):
        self.firstTurn=None
        self.houseRules=[None]
        self.currentTurn=0
        self.amountOfPlayers=4
        self.highscores=None
        self.reverse=False

    def start(self):
        player.name=input("Welcome to FPS UNO (FPS not included), Please Input Your Name: ")
        #begins the game
        print("The game will now start")
        player.startingHand(player)
        opponent.oppstartingHand(opponent)
        print("You draw your hand")
        print(player.hand)
    
    def firstturn(self):
        if "1" in self.firstTurn:
            action=input("it is your turn, type the card you would like to play, if you have no available cards, type draw")
            if "draw" in input:
                deck.draw_function()
        else:
            print("the AI are taking their turns, please wait ")

    def playCards(card,self): #BUG add more to reverse and draw two cards
        topdisc=card
        if "skip" in card:
            if self.reverse is True:
                self.currentTurn-=1
            else:
                self.currentTurn+=1
        elif "reverse" in card:
            print("The turn order has been reversed")
            if self.reverse is True:
                self.reverse=False
                self.currentTurn+=1
            else:
                self.reverse=True
                self.currentTurn-=1
            #make this count backward for turns
        elif "draw two" in card:
            if self.currentTurn==0:
                print("You have been skipped")
            else:
                print(f"{playerList[self.currentTurn]} has been skipped")
            if self.reverse==False:
                self.currentTurn+=1
            else:
                self.currentTurn-=1
            for i in range(0,len(playerList)):
                #BUG make the next player draw two cards and skip their turn
                return None

    






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
                        player.hand.append(self.drawnCard)
                elif tempCard[0]==tempCardTwo[0] or tempCard[1]==tempCardTwo[1]:
                    print(f"Your card matches the {topdisc} in the discards, would you like to play it?")
                    playChoice=input("y/n ")
                    if playChoice=="y":
                        game.playCards(self.drawnCard)
                    else:
                        player.hand.append(self.drawnCard)

    def checkForMatchingCard(self): #BUG finish this (also deck.topdisc doesnt exist for some reason)
        availableCards=[]
        for i in range(0,len(player.hand)):
            tempCard=topdisc.split(" ")
            tempCardTwo=player.hand[i].split(" ")
            if tempCardTwo[0]=="wild" or tempCard[0]==tempCardTwo[0] or tempCard[1]==tempCardTwo[1]:
                availableCards.append(player.hand[i])
        if len(availableCards)>=1:
            gameInput=input(f"These {availableCards} match the discards, would you like to play one or draw? (play [card name]/draw) ")
            if "play" in gameInput.lower():
                game.playCards(card,game)
            elif "draw" in gameInput.lower():
                deck.draw_function(deck)
            else:
                deck.checkForMatchingCard()
        else:
            print("You do not have any matching cards, you must draw")
            deck.draw_function(deck)

    def firstCardAction():
        #make this do something if the first card is a special action


        return None
        
def createPlayerList():
    

def main():
    uno=game()
    unoCard=card()
    unoDeck=deck()
    Player=player()
    oppOne=opponent()
    oppTwo=opponent()
    oppThree=opponent()
    
    global topdisc
    global playerList
    topdisc=card.cardSelection(card)
    

    



    uno.start()
    playerList=[player.name,oppOne.name,oppTwo.name,oppThree.name]
    print(playerList)
    print(f"The first card is {topdisc}")
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
