"""
@author: Aleph Aseffa
"""


class Card:
    def __init__(self, card_name, color_group, card_cost, house_cost, houses_built, rent_prices, mortgage_amt, owner, mortgaged):
        self.card_name = card_name                  # str
        self.color_group = color_group              # str
        self.card_cost = card_cost                  # int
        self.house_cost = house_cost                # int
        self.houses_built = houses_built            # int
        self.rent_prices = rent_prices              # int
        self.mortgage_amt = mortgage_amt            # int
        self.owner = owner                          # str
        self.mortgaged = mortgaged                  # bool

    def mortgage(self, player):
        player.add_balance(self.mortgage_amt)
        self.mortgaged = True

    def sell(self, player):
        player.add_balance(self.card_cost)
        self.owner = 'Bank'

    def purchase_card(self, player):
        if self.card_cost > player.balance:
            print("You cannot afford this card at the moment.")
        else:
            player.cards_owned.append(self)
            player.reduce_balance(self.card_cost)
            self.owner = player