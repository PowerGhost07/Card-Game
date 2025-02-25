# This Program will be used to develop the framework that is behind the actual graphics
# The code must be as dead simple, easy to understand, and modifiable

import random
import os

line = "----------" # number of dashes per line that seperates each message as game progresses

newDeck = [
    [1, "s"], [2, "s"], [3, "s"], [4, "s"], [5, "s"], [6, "s"], [7, "s"], [8, "s"], [9, "s"], [10, "s"], [11, "s"], [12, "s"], [13, "s"], 
    [1, "h"], [2, "h"], [3, "h"], [4, "h"], [5, "h"], [6, "h"], [7, "h"], [8, "h"], [9, "h"], [10, "h"], [11, "h"], [12, "h"], [13, "h"], 
    [1, "d"], [2, "d"], [3, "d"], [4, "d"], [5, "d"], [6, "d"], [7, "d"], [8, "d"], [9, "d"], [10, "d"], [11, "d"], [12, "d"], [13, "d"], 
    [1, "c"], [2, "c"], [3, "c"], [4, "c"], [5, "c"], [6, "c"], [7, "c"], [8, "c"], [9, "c"], [10, "c"], [11, "c"], [12, "c"], [13, "c"]]

def introduction(): # clears screen then prints a greeting
    global line
    os.system('cls') 
    print("Welcome to Black Jack Text Prototype")
    print(line)

def isBetValid(amount): # returns True or False if amount is valid or invalid respectively
    global money # calls the global variable "money"
    try: # non number detection
        amount = float(amount) # attempts to convert the argument to a float to pick out an error before it errors in the if statement instead

        if amount <= 0 or amount > money: # returns False if the amount is not acceptable
            return False
        else:
            return True
        
    except ValueError: # returns False if the amount is not readable
        return False

def pullCard(deck): # pops a random item from the list of cards and returns that popped item
    randomPosition = random.choice(0, len(deck)-1)
    card = newDeck.pop(randomPosition)
    return card

def getCardValue(card):
    return card[0][0]



def readOutTable():
    global dealerCards
    global playerCards

    for card in range(len(dealerCards)):
        if getCardValue(card) > 10:
            card = 10
        

    print(line)
    print(f"Dealer Cards: {}")

running = True # variable that keeps game loop running

money = 100 # starting amount of money

dealerCards = []
playerCards = []

introduction()
while running: # game loop

    
    betting = True # initializes betting loop
    while betting: # betting loop keeps stating how much money the player has and asks for a valid bet until the input is valid
        print(f"You have ${money}\n{line}")
        answer = input("How much would you like to bet?: ")
        if isBetValid(answer):
            bet = answer
            print(f"You have bet ${bet}")
            betting = False
        else:
            print(f"Your bet of ${answer} if not possible")
        print(line)
    
    # inittializes 2 cards for the dealer and 2 cards for the player before the start of the game
    dealerCards.append(pullCard(newDeck))
    dealerCards.append(pullCard(newDeck))
    playerCards.append(pullCard(newDeck))
    playerCards.append(pullCard(newDeck))

    playing = True
    while playing:
        
