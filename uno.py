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
        self.currentTurn=None
        self.amountOfPlayers=4
        self.highscores=None
        self.playerList=[None]
        self.reverse=False

    
    def start(self):
        gamestart=False
        startlist="1.Start Game | 2.Edit House Rules | 3.View Highscores"
 
        player.name=input("Welcome to FPS UNO (FPS not included), Please Input Your Name: ")
        while gamestart is False:
            print("type the number of your choice ")
            print(startlist)
            userinput=str(input())
 
            if "1" in userinput:
                #begins the game
                print("the game will now start")
                gamestart=True
                player.startingHand(player)
                opponent.oppstartingHand(opponent)
                print("You draw your hand")
                print(player.hand)


            elif "2" in userinput:
                seconduserinput=input("1.edit drawrule 2.toggle 7s switch hands ")
 
                if "1" in seconduserinput:
                    print("Input your drawrule (how many times you want to draw)")
                    deck.drawrule=int(input())
                elif "2" in seconduserinput:
                    value=0
                    value+=1
                    if value==2:
                        print("Number 7 cards are now disabled")
                        self.houseRules=False
                    print("Number 7 cards now allow you to switch hands with a player of your choice")
                    self.houseRules=True
 
            elif "3" in userinput:
                print("FIX THIS WHEN YOU MAKE THE CODE THAT READS THE FILE") #BUG
    
 def firstturn(self):
        d=deck()
        if "1" in self.firstTurn:
            action=input("it is your turn, type the card you would like to play, if you have no available cards, type draw")
            if "draw" in input:
                d.draw_function()
        else:
            print("the AI are taking their turns, please wait ")
        return None

    def playCards(card,self): #BUG add more to reverse and draw two cards
        deck.topdisc=card
        if "skip" in card:
            self.currentTurn+=1
        elif "reverse" in card:
            self.currentTurn-=1
            self.reverse=True
            #make this count backward for turns
        elif "draw two" in card:
            if self.reverse==False:
                self.currentTurn+=1
            else:
                self.currentTurn-=1
            for i in range(0,len(game.playerList)):
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
        self.drawrule=1
        self.drawnCard=None
        self.topdisc=card.cardSelection(card)


    def draw_function(self): #BUG make this hook into the play card function so you can play cards if you draw
            for i in range(0,self.drawrule):
                self.drawnCard=card.cardSelection(card)
                print(f"You draw a card, your card is {self.drawnCard}")
                
                tempCard=self.drawnCard.split(" ")
                tempCardTwo=self.topdisc.split(" ")
                if tempCard[0]=="wild":
                    print(f"Your card is a wild, would you like to play it?")
                    playChoice=input("y/n ")
                    if playChoice=="y":
                        deck.playCards()
                        
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

    def checkForMatchingCard(card,self): #BUG finish this (also deck.topdisc doesnt exist for some reason)
        for i in range(0,len(player.hand)):
            tempCard=self.topdisc.split(" ")
            tempCardTwo=player.hand[i].split(" ")
            if tempCard[0]=="wild":
                print(f"Your card is a wild, would you like to play it?")
                playChoice=input("(y/n) ")
                if playChoice=="y":
                    deck.playCards()
        gameInput=input(f"Your cards match the {self.topdisc} in the discards, would you like to play one or draw? (play/Draw) ")
        if "play" in gameInput:
            game.playCards(card)
        elif "draw" in gameInput.lower() or "" in gameInput:
            deck.draw_function()
        


def main():
    uno=game()
    unoCard=card()
    unoDeck=deck()
    Player=player()
    oppOne=opponent()
    oppTwo=opponent()
    oppThree=opponent()
    
    uno.start()
    uno.playerList=[Player.name,oppOne.name,oppTwo.name,oppThree.name]
    print(f"The first card is {unoDeck.topdisc}")
    unoDeck.checkForMatchingCard(unoDeck)



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
        self.currentTurn=None
        self.amountOfPlayers=4
        self.highscores=None
        self.playerList=[None]
        self.reverse=False

    
    def start(self):
        gamestart=False
        startlist="1.Start Game | 2.View Highscores"
 
        player.name=input("Welcome to FPS UNO (FPS not included), Please Input Your Name: ")
        #begins the game
        print("The game will now start")
        gamestart=True
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
            self.currentTurn+=1
        elif "reverse" in card:
            self.currentTurn-=1
            self.reverse=True
            #make this count backward for turns
        elif "draw two" in card:
            if self.reverse==False:
                self.currentTurn+=1
            else:
                self.currentTurn-=1
            for i in range(0,len(game.playerList)):
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
                        game.playCards()
                        
                    else:
                        player.addToHand(self.drawnCard,player)
                elif tempCard[0]==tempCardTwo[0] or tempCard[1]==tempCardTwo[1]:
                    print(f"Your card matches the {topdisc} in the discards, would you like to play it?")
                    playChoice=input("y/n ")
                    if playChoice=="y":
                        #BUG make this play card
                        return None
                    else:
                        player.addToHand(self.drawnCard,player)

    def checkForMatchingCard(card,self): #BUG finish this (also deck.topdisc doesnt exist for some reason)
        for i in range(0,len(player.hand)):
            tempCard=topdisc.split(" ")
            tempCardTwo=player.hand[i].split(" ")
            if tempCardTwo[0]=="wild" or tempCard[0]==tempCardTwo[0] or tempCard[1]==tempCardTwo[1]:
                gameInput=input(f"Your cards match the {topdisc} in the discards, would you like to play one or draw? (play/Draw) ")
                if "play" in gameInput:
                    game.playCards(card)
                elif "draw" in gameInput.lower() or "" in gameInput:
                    deck.draw_function(deck)
            else:
                print("You do not have any matching cards, you must draw")
                deck.draw_function(deck)
        


def main():
    uno=game()
    unoCard=card()
    unoDeck=deck()
    Player=player()
    oppOne=opponent()
    oppTwo=opponent()
    oppThree=opponent()
    
    global topdisc
    topdisc=card.cardSelection(card)

    uno.start()
    uno.playerList=[Player.name,oppOne.name,oppTwo.name,oppThree.name]
    print(f"The first card is {topdisc}")
    unoDeck.checkForMatchingCard(unoDeck)



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
