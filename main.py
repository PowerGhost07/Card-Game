from table import *
from settings import *

import pygame

pygame.init()

deck = CardDeck().shuffled_deck

player_one = Player(STARTING_MONEY)

player_one_hand = player_one.hand

for i in range(5):
    player_one_hand.append(deck[i])

print(player_one_hand)
