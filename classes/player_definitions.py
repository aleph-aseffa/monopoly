"""
@author: Aleph Aseffa
Date created: 7/14/2019

Contains the Player class and associated functions.
"""
import random
#from ai import ai


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
        Simulates the randomness of throwing two die.
        :return: n: an int between 2 and 12 inclusive.
        """
        random.seed()
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        n = dice1 + dice2
        print(f"{self.name} threw {n}")
        return n

    def move_player(self, dice_amt):
        """
        Moves the player by the amount returned by rolling two die.
        :param dice_amt: int, the number rolled by the two die.
        :return: an int that represents the updated position of the player on the board.
        """
        self.current_pos += dice_amt
        return self.current_pos

    def check_pos(self, board):
        """
        Checks what card the player has landed on and carries out the appropriate action.
        :param board: list, the monopoly board.
        :return: None
        """
        self.current_pos = self.current_pos % 40
        brd_property = board[self.current_pos]

        if brd_property.card_cost == "N/A":  # this means the player cannot purchase the card

            if brd_property.card_name == 'Jail/Visiting Jail':
                print(f"{self.name} is visiting jail.")

            elif brd_property.card_name == 'Luxury Tax':
                print(f"{self.name} landed on Luxury Tax and has been fined $75")
                self.reduce_balance(75)

            elif brd_property.card_name == 'Income Tax':
                print(f"{self.name} landed on Income Tax and has been fined $200")
                self.reduce_balance(200)

            elif brd_property.card_name == 'Go to Jail':
                print(f"{self.name} landed on Go to Jail and has been arrested!")
                self.send_to_jail()

            else:
                print(f"{self.name} landed on {brd_property.card_name}")

        else:
            if brd_property.mortgaged:
                print(f"{self.name} landed on a mortgaged property.")

            elif brd_property.owner != 'Bank': # and brd_property.owner.name != self.name:
                if brd_property.owner.name == self.name:
                    print(f"{self.name} landed on {brd_property.card_name}, a property they own.")
                else:
                    print(f"{self.name} landed on {brd_property.card_name}, a property owned by {brd_property.owner.name}")
                    self.charge_rent(brd_property)

            else:
                print(f"{self.name} landed on {brd_property.card_name}")
                if self.name == "AI":
                    return 1  # Indicates to the AI that the property can be purchased
                else:
                    user_action = input("Do you want to buy the property? (y/n) ")
                    if user_action == 'y':
                        brd_property.purchase_card(self)

    def add_balance(self, amount):
        """
        Increases the player's balance.
        :param amount: int, the amount of money to add to the player's balance.
        :return: self.balance: the updated balance of the player.
        """
        self.balance += amount
        return self.balance

    def charge_rent(self, card):
        """
        Charges the rent cost to the player.
        :param card: an instance of the Card class.
        :return: None.
        """
        if card.color_group == "Railroad":
            rent_amt = 25 * card.owner.railroads_owned
        else:
            rent_amt = card.rent_prices[1]
        print(f"{self.name} is paying ${rent_amt} as a rental charge to {card.owner.name}")
        self.reduce_balance(rent_amt)
        card.owner.add_balance(rent_amt)

    def reduce_balance(self, amount):
        """
        Reduces the player's balance.
        :param amount: int, the amount of money to reduce the player's balance by.
        :return: None.
        """
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
        """
        Bank collects all the player's owned properties and sets their bankruptcy status to True.
        :return: None.
        """
        self.balance = 0

        if len(self.cards_owned):
            for card in self.cards_owned:
                card.owner = "Bank"
        self.railroads_owned = 0

        self.bankruptcy_status = True

    def check_if_bankrupt(self, amt_owed):
        """
        Checks if the player is bankrupt (i.e. can the player afford what they are being charged?).
        :param amt_owed: int, the amount the player is being charged.
        :return: Bool that represents if the player is bankrupt or not.
        """
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
        """
        Prints out all the cards the player owns.
        :return: None.
        """
        total = 0
        for card in self.cards_owned:
            print(f"{card.card_name}: ${card.card_cost}")
            total += card.card_cost
        print(f"The sum of your card costs is: ${total}")

    def player_action(self, user_choice):
        """
        Takes in the user's choice of what action to take and carries out that action.
        :param user_choice: char, what the player chooses to do (e.g. r to roll the dice).
        :return: None.
        """
        # TODO: add sell, mortgage, and construct house functions.
        val = -1
        if user_choice == "r":
            val = self.roll_dice()
        elif user_choice == "b":
            print(f"Your balance is: ${self.balance}")
        elif user_choice == "c":
            print("Your properties are:")
            self.display_player_properties()
        elif user_choice == "s":
            print("Sell property feature coming soon.")
        elif user_choice == "m":
            print("Mortgage property feature coming soon.")
        elif user_choice == "h":
            print("Construct house feature coming soon.")
        else:
            print("Please enter a valid command.")

        return val

    def send_to_jail(self):
        """
        Sends the player to jail.
        :return: None.
        """
        self.current_pos = 10
        self.doubles_counter = 0

    def release_from_jail(self):
        """
        Releases the player from jail.
        :return: None.
        """
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

    def trade_with_human(self, other_player):  # TODO: finish function
        cash_value = input("How much cash do you want to offer? ")
        properties_to_offer = input("Enter the properties do you want to offer separated by commas\n").split(',')
        cash_received = input(f"How much cash is {other_player.name} giving you?")
        properties_received = input(f"Which properties is {other_player.name} giving you?\n").split(',')

        pass

    def trade_with_ai(self):  # TODO: finish function
        cash_value = input("How much cash do you want to offer? ")
        properties_to_offer = input("Enter the properties do you want to offer separated by commas\n").split(',')

        if ai.evaluate_trade(self, cash_value, properties_to_offer):
            pass
        else:
            retry = input("The AI has rejected your trade offer. Do you want to suggest a different trade? (y/n")
            if retry == "y":
                self.trade_with_ai()
