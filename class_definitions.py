"""
@author: Aleph Aseffa
Date created: 7/14/2019

Contains all the classes of the game.

Note: Currently there is no option to buy houses and hotels.

"""
import random
import card_definitions as c_def


Board = {
    0: 'Park Place',
    1: 'Community Chest',
    2: 'Chance',
    3: 'Ventnor Avenue',
    4: 'Go to Jail'
}


class Player:
    def __init__(self, name, balance, cards_owned, current_pos, in_jail, railroads_owned, doubles_counter, amount_owed, bankruptcy_status):
        self.name = name                            # str
        self.balance = balance                      # int
        self.cards_owned = cards_owned              # list
        self.current_pos = current_pos              # int (index)
        self.in_jail = in_jail                      # bool
        self.railroads_owned = railroads_owned      # int
        self.doubles_counter = doubles_counter      # int
        self.amount_owed = amount_owed              # int
        self.bankruptcy_status = bankruptcy_status  # bool

    def roll_dice(self):  # TODO: add check for doubles.
        """
        :return: n, an int between 2 and 12 inclusive.
        """
        random.seed()
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        n = dice1 + dice2
        print(f"{self.name} threw {n}")
        return n

    def move_player(self, dice_amt):
        """
        :param dice_amt: int, the number rolled by the two dice.
        :return: an int that represents the updated position of the player on the board.
        """
        self.current_pos += dice_amt
        return self.current_pos

    def check_pos(self, board):  # TODO: Clean up this function.
        """
        :param board: list, the monopoly board
        :return: none
        """
        self.current_pos = self.current_pos % 40
        brd_property = board[self.current_pos]

        if brd_property.card_name == 'Community Chest':
            print(f"{self.name} landed on Community Chest")  # TODO: add all these functions
        elif brd_property.card_name == 'Chance':
            print(f"{self.name} landed on Chance")
        elif brd_property.card_name == 'Jail/Visiting Jail':
            print(f"{self.name} is visiting jail.")
        elif brd_property.card_name == 'Luxury Tax':
            print(f"{self.name} landed on Luxury Tax and has been fined $75")
            self.reduce_balance(75)
        elif brd_property.card_name == 'Income Tax':
            print(f"{self.name} landed on Income Tax and has been fined $200.")
            self.reduce_balance(200)
        elif brd_property.card_name == 'Go to Jail':
            print(f"{self.name} landed on Go to Jail and has been arrested!")
            self.send_to_jail()
        elif brd_property.card_name == 'Go':
            print(f"{self.name} landed on Go.")
        elif brd_property.mortgaged:
            print(f"{self.name} landed on a mortgaged property.")
        elif brd_property.owner != 'Bank' and brd_property.owner.name != self.name:
            print(f"{self.name} landed on a property owned by {brd_property.owner.name}")
            self.charge_rent(brd_property)
        else:
            print(f"{self.name} landed on {brd_property.card_name}")
            user_action = input("Do you want to buy the property? (y/n) ")
            if user_action == 'y':
                brd_property.purchase_card(self)

    def add_balance(self, amount):
        """
        Increases the player's balance
        :param amount: int, the amount of money to add to the player's balance
        :return: self.balance: the updated balance of the player
        """
        self.balance += amount
        return self.balance

    def charge_rent(self, card):
        if card.color_group == "Railroad":
            rent_amt = 25 * card.owner.railroads_owned
        else:
            rent_amt = card.rent_prices[1]
        print(f"{self.name} is paying ${rent_amt} as a rental charge to {card.owner.name}")
        self.reduce_balance(rent_amt)
        card.owner.add_balance(rent_amt)

    def reduce_balance(self, amount):
        if self.balance < amount:
            print("Your balance is insufficient for this action.")
            bankrupt = self.check_if_bankrupt(amount)
            if not bankrupt:
                print("You need to sell or mortgage certain properties.")
                user_action = input("Do you want to sell or mortgage? (s/m)")
                if user_action == 's':
                    pass  # sell()  TODO: implement this function.
                else:
                    pass  # mortgage()  TODO: implement this function.
        else:
            self.balance -= amount

    def bankrupt_player(self):
        self.balance = 0

        if len(self.cards_owned):
            for card in self.cards_owned:
                card.owner = "Bank"
        self.railroads_owned = 0

        self.bankruptcy_status = True

    def check_if_bankrupt(self, amt_owed):
        net_worth = 0

        for card in self.cards_owned:
            if card.mortgaged:
                net_worth -= card.mortgage_amt
                net_worth += card.card_cost
            else:
                net_worth += card.card_cost

        if (self.balance + net_worth) < amt_owed:
            print(f"Unfortunately, {self.name} is now bankrupt! It's game over for them!")
            self.bankrupt_player()
            return True
        else:
            return False

    def display_player_properties(self):
        total = 0
        for card in self.cards_owned:
            print(f"{card.card_name}: ${card.card_cost}")
            total += card.card_cost
        print(f"The sum of your card costs is: {total}")

    def player_action(self, user_choice):
        if user_choice == "b":
            print(self.balance)
            return -1
        elif user_choice == "c":
            self.display_player_properties()
            return -1
        elif user_choice == "s":

            # TODO: Implement sell_property function
            return -1
        elif user_choice == "m":
            mortgage_card_name = input("Enter the name of the card you want to mortgage. ")
            c_def.find_card(mortgage_card_name)

        else:
            dice_val = self.roll_dice()
            return dice_val

    def send_to_jail(self):
        self.current_pos = 10
        self.doubles_counter = 0

    def release_from_jail(self):
        self.doubles_counter = 0
        bail_choice = input("Would you like to pay the $50 bail? (y/n) ")
        if bail_choice == "y":
            self.reduce_balance(50)
            self.in_jail = False
            dice_result = self.roll_dice()
            self.move_player(dice_result)
        else:
            self.roll_dice()
            if self.doubles_counter == 1:
                self.doubles_counter = 0
                dice_result = self.roll_dice()
                self.move_player(dice_result)

