import random
#
#
#
#
#
#

newDeck = [
    [1, "s"], [2, "s"], [3, "s"], [4, "s"], [5, "s"], [6, "s"], [7, "s"], [8, "s"], [9, "s"], [10, "s"], [11, "s"], [12, "s"], [13, "s"], 
    [1, "h"], [2, "h"], [3, "h"], [4, "h"], [5, "h"], [6, "h"], [7, "h"], [8, "h"], [9, "h"], [10, "h"], [11, "h"], [12, "h"], [13, "h"], 
    [1, "d"], [2, "d"], [3, "d"], [4, "d"], [5, "d"], [6, "d"], [7, "d"], [8, "d"], [9, "d"], [10, "d"], [11, "d"], [12, "d"], [13, "d"], 
    [1, "c"], [2, "c"], [3, "c"], [4, "c"], [5, "c"], [6, "c"], [7, "c"], [8, "c"], [9, "c"], [10, "c"], [11, "c"], [12, "c"], [13, "c"]]

def drawCard(list):
    card = list.pop(0)
    return card


def getCardValue(card):
    return card[0]

def getTotalValue(hand):

    listOfRawValues = [] # initializes a list to store values of cards with aces that are all still worth 1
    totalValue = 0
    
    for card in hand: # populates listOfRawValues with only the integer value of the cards values
        listOfRawValues.append(getCardValue(card))

    print(listOfRawValues) # debug

    for value in listOfRawValues:
        if value == 1:
            testTotalValue = (sum(listOfRawValues))+10

            if testTotalValue <= 21 and testTotalValue > totalValue:
                totalValue = testTotalValue
        else:
            totalValue = sum(listOfRawValues)
    
    return totalValue

myHand = [[1, "d"], [1, "d"], [2, "d"], [4, "d"]]
print(getTotalValue(myHand))
            




