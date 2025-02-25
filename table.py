import random


class CardDeck:
    def __init__(self):
        self.suits = ["c", "d", "h", "s"]
        self.ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
        self.new_deck_order = self.generate_deck()
        self.shuffled_deck = self.generate_shuffled_deck()


    def generate_deck(self):
        list = []
        for suit in self.suits:
            for rank in self.ranks:
                list.append([rank, suit])
        return list
    
    def generate_shuffled_deck(self):
        list = self.generate_deck()
        new_list = []
        for card in range(len(list)):
            new_list.append(random.choice(list))
        return new_list

class Dealer:
    def __init__(self):
        self.start_betting = False
        self.stop_betting = False
        self.start_dealing = False
        self.stop_dealing = False
        self.declare_winner = False

class Player:

    def __init__(self, money):
        self.money = money
        self.bet = None
        self.hitting = False
        self.standing = False
        self.earnings = None
        self.hand = []

deck = CardDeck()