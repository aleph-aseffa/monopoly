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
        """
        Sets the card's mortgaged status to True and updates the player's balance.
        :param player: An instance of the Player class.
        :return: None.
        """
        player.add_balance(self.mortgage_amt)
        self.mortgaged = True

    def sell(self, player):
        """
        Returns ownership of the card to the Bank and updates the player's balance.
        :param player: An instance of the Player class.
        :return: None.
        """
        player.add_balance(self.card_cost)
        self.owner = 'Bank'

    def purchase_card(self, player):
        """
        Gives ownership of the card to the Bank and updates the player's balance.
        :param player: An instance of the Player class.
        :return: None.
        """
        if self.card_cost > player.balance:
            print("You cannot afford this card at the moment.")
        else:
            player.cards_owned.append(self)
            player.reduce_balance(self.card_cost)
            self.owner = player

    def construct_house(self, player):
        """
        Updates number of houses that have been built on the card.
        :param player: An instance of the Player class.
        :return: None.
        """
        if self.house_cost > player.balance:
            print("You cannot afford a house on this property at the moment.")
        elif self.houses_built == 5:
            print("You have built the maximum number of houses on this property.")
        else:
            self.houses_built += 1
            print(f"You have built a house on {self.card_name}.")


def locate_card_object(name, board):

    for card in board:
        if card.card_name == name:
            card_object = card
            break

    return card_object
