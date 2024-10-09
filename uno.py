import random, time

COLORS = ['red', 'yellow', 'green', 'blue', 'wild']
TYPES = ['reverse', 'skip', 'draw two']
AI_NAMES = ["HAL", "Dave", "ChatGPT", "GLaDOS", "Elvis", "Bob", "Jim", "Rat", "John"]

# create a functioning uno game
# implement "AI" opps
# track hands and discards
# function to play cards that match discards
# function to draw cards and remove from deck
# set win condition and end game
# implement optional house rules
# add a timer between print statements for better ux

class Bot():
    def __init__(self):
        self.name = None
        self.hand = []
    
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

def find_matches(topcard, hand):
    matching_cards = []
    topcard_split = topcard.split(" ")
    for card in hand:
        card_split = card.split(" ")
        if card_split[0] == "wild" or topcard_split[0] == card_split[0] or topcard_split[1] == card_split[1]:
            matching_cards.append(card)
    return matching_cards

def initialize_game(deck, bot_one, bot_two, bot_three):
    Player.name = input("Welcome to UNO in Python, please input your name: ")
    bot_one.create_ai_names()
    bot_two.create_ai_names()
    bot_three.create_ai_names()
    for i in range(7):
        draw(deck, Player.hand)
        draw(deck, bot_one.hand)
        draw(deck, bot_two.hand)
        draw(deck, bot_three.hand)

def increment_turn(current_turn, reverse):
    if reverse:
        if current_turn == 1:
            current_turn = 4
        else:
            current_turn -= 1
    else:
        if current_turn == 4:
            current_turn = 1
        else:
            current_turn += 1

def play_card(card, deck, hand):
    hand.remove(card)
    deck.append(card)

def turn_logic(current_turn, topcard, deck, bot_one, bot_two, bot_three):
    if current_turn == 1:
        matching_cards = find_matches(topcard, Player.hand)
        print(f"Your hand: {Player.hand}")
        time.sleep(0.5)
        if len(matching_cards) > 0:
            print(f"The top card is a {topcard}.")
            time.sleep(0.5)
            print(f"Your matching cards are: {matching_cards}")
            time.sleep(0.5)
            user_action = input("What would you like to do? (draw/play <card>)\n>> ")
            if user_action.lower() == "draw":
                draw(deck, Player.hand)
            elif ((user_action.lower()).split(" "))[0] == "play":
                play_card(((user_action.lower()).split("play "))[0], deck, Player.hand)
                # ^ does not work "ValueError: list.remove(x): x not in list"
                # maybe change the parameters used for play_card() to something that actually matches the card name

def gameplay_loop():
    deck = create_deck()
    bot_one = Bot()
    bot_two = Bot()
    bot_three = Bot()

    initialize_game(deck, bot_one, bot_two, bot_three)
    time.sleep(1)
    print("The game is starting...")
    current_turn = 1
    reverse = False
    time.sleep(1)
    #while True:
        # run game until player or bot wins
        

        #return None
    turn_logic(current_turn, deck[len(deck)-1], deck, bot_one, bot_two, bot_three)
    increment_turn(current_turn, reverse)
        
def main():
    gameplay_loop()

if __name__ == "__main__":
    main()