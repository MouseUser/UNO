import random, time

COLORS = ['red', 'yellow', 'green', 'blue', 'wild']
TYPES = ['reverse', 'skip', 'draw two']
AI_NAMES = ["HAL", "Dave", "ChatGPT", "GLaDOS", "Elvis", "Bob", "Jim", "Rat", "John"]

# create a functioning uno game
# implement "AI" opps (fix their hands)
# track hands and discards
# function to play cards that match discards
# function to draw cards and remove from deck
# set win condition and end game
# implement optional house rules
# add a timer between print statements for better ux

class Bot():
    hand = []
    def __init__(self):
        self.name = None
    
    def create_ai_names(self):
        self.name = random.choice(AI_NAMES)
        AI_NAMES.remove(self.name)

class Player():
    hand = []
    def __init__(self):
        self.name = None

def create_deck():
    deck = []
    for i in range(2):
        for red in range(13):
            if red <= 9:
                deck.append("red " + str(red))
            else:
                deck.append("red " + TYPES[red - 10])
        
        for yellow in range(13):
            if yellow <= 9:
                deck.append("yellow " + str(yellow))
            else:
                deck.append("yellow " + TYPES[yellow - 10])

        for blue in range(13):
            if blue <= 9:
                deck.append("blue " + str(blue))
            else:
                deck.append("blue " + TYPES[blue - 10])
        
        for green in range(13):
            if green <= 9:
                deck.append("green " + str(green))
            else:
                deck.append("green " + TYPES[green - 10])
        
        for wild in range(2):
            deck.append("wild normal")
            deck.append("wild draw four")
    
    shuffle(deck)
    return deck

def shuffle(deck):
    random.shuffle(deck)
    return deck

def draw(deck, hand):
    hand.append(deck.pop())

def initialize_game(deck, bot_one, bot_two, bot_three):
    Player.name = input("Welcome to UNO in Python, please input your name: ")
    for i in range(7):
        draw(deck, Player.hand)
        draw(deck, bot_one.hand)
        draw(deck, bot_two.hand)
        draw(deck, bot_three.hand)

def gameplay_loop():
    deck = create_deck()
    bot_one = Bot()
    bot_two = Bot()
    bot_three = Bot()

    

    initialize_game(deck, bot_one, bot_two, bot_three)
    print("bot two hand:")
    print(bot_two.hand)
    while True:
        # run game until player or bot wins
        return None
        

def main():
    gameplay_loop()

if __name__ == "__main__":
    main()