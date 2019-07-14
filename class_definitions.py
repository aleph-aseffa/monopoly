"""
@author: Aleph Aseffa
Date created: 7/14/2019

Contains all the classes of the game.

Note: Currently there is no option to buy houses and hotels.

"""
import random


Board = {
    0: 'Park Place',
    1: 'Community Chest',
    2: 'Chance',
    3: 'Ventnor Avenue',
    4: 'Go to Jail'
}


class Player:
    def __init__(self, name, balance, cards_owned, current_pos, in_jail, railroads_owned):
        self.name = name                            # str
        self.balance = balance                      # int
        self.cards_owned = cards_owned              # list
        self.current_pos = current_pos              # int (index)
        self.in_jail = in_jail                      # bool
        self.railroads_owned = railroads_owned      # int

    # Other functions

    # TODO: Check if a double was thrown.
    def roll_dice(self):
        random.seed()
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        n = dice1 + dice2
        print(f"{self.name} threw {n}")
        return n

    def move_player(self, dice_amt):
        self.current_pos += dice_amt
        return self.current_pos

    def check_pos(self, board):  # TODO: fix the board issue (modulo)
        self.current_pos = self.current_pos % 5
        brd_property = board[self.current_pos]

        if brd_property.card_name == 'Community Chest':
            print(f"{self.name} landed on Community Chest")  # TODO: add all these functions
        elif brd_property.card_name == 'Chance':
            print(f"{self.name} landed on Chance")
        elif brd_property.card_name == 'Luxury Tax':
            print(f"{self.name} landed on Luxury Tax")
        elif brd_property.card_name == 'Income Tax':
            print(f"{self.name} landed on Income Tax")
        elif brd_property.card_name == 'Go to Jail':
            print(f"{self.name} landed on Go to Jail")
        elif brd_property.mortgaged:
            print(f"{self.name} landed on a mortgaged property.")
        elif brd_property.owner != 'Bank':
            print(f"{self.name} landed on a property owned by {brd_property.owner}")
        else:
            user_action = input("Do you want to buy the property? (y/n) ")
            if user_action == 'y':
                # purchase_property()
                pass
            else:
                pass

    def add_balance(self, amount):
        self.balance += amount

    def reduce_balance(self, amount):
        if self.balance < amount:
            print("Your balance is insufficient for this action.")
            user_action = input("Would you like to trade with another player? (y/n ")
            if user_action == 'y':
                # trade()
                pass
            bankruptcy_status = False  # TODO: remove this line once the function has been implemented.
            # bankruptcy_status = check_if_bankrupt()
            if bankruptcy_status:
                pass # bankrupt_player()  TODO: implement this function.
            else:
                print("You need to sell or mortgage certain properties.")
                user_action = input("Do you want to sell or mortgage? (s/m)") # TODO: add option to sell just houses and hotels.
                if user_action == 's':
                    pass # sell()  TODO: implement this function.
                else:
                    pass # mortgage()  TODO: implement this function.

    def mortgage(self, card):  # TODO: fix this, maybe take in a list?
        self.add_balance(card.mortgage_amt)
        card.mortgaged = True

    def sell(self, card):  # TODO: maybe take in a list?
        self.add_balance(card.card_cost)
        card.owner = 'Bank'

    def check_if_bankrupt(self, balance, amt_owed):
        net_worth = 0

        for card in self.cards_owned:
            if card.mortgaged:
                net_worth -= card.mortgage_amt
                net_worth += card.card_cost
            else:
                net_worth += card.card_cost

        if (balance + net_worth) < amt_owed:
            return True
        else:
            return False

    # def purchase_card(self):


class Card:
    def __init__(self, card_name, color_group, card_cost, house_cost, rent_prices, mortgage_amt, owner, mortgaged):
        self.card_name = card_name                  # str
        self.color_group = color_group              # str
        self.card_cost = card_cost                  # int
        self.house_cost = house_cost                # int
        self.rent_prices = rent_prices              # int
        self.mortgage_amt = mortgage_amt            # int
        self.owner = owner                          # str/int TODO: decide this
        self.mortgaged = mortgaged                  # bool




