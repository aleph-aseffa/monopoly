"""
Contains the code for the AI that can play against the user.
"""
from classes import card_definitions as c_def


def move(ai, board):

    if ai.in_jail:
        leave_jail(ai, board)

    dice_roll = ai.roll_dice()
    ai.move_player(dice_roll)
    curr_card = board[ai.current_pos % 40]
    purchasable = ai.check_pos(board)

    if purchasable and ai.balance > curr_card.card_cost:
        curr_card.purchase_card(ai)
        print(f"{ai.name} has purchased {curr_card.card_name}")


def leave_jail(ai, board):
    ai.reduce_balance(50)
    ai.in_jail = False
    print(f"{ai.name} has paid the $50 bail and has been released from jail.")
    move(ai, board)


# TODO: evaluate what the human gains from the trade and factor that into the cost/benefit analysis.
def evaluate_trade(human, ai, money_offered, properties_offered, money_wanted, properties_wanted, board):
    personal_gain = 0
    human_gain = 0

    properties_valuation_personal = 0

    benefit = 0

    if ai.balance < 200:
        multiplier = 5
    else:
        multiplier = 2.5

    # evaluate the value of the properties to be exchanged:
    if properties_offered[0] == '':
        pass
    else:
        for card_name in properties_offered:
            card_object = c_def.locate_card_object(card_name, board)
            personal_gain += card_object.card_cost

    if properties_wanted[0] == '':
        pass
    else:
        for card_name in properties_wanted:
            card_object = c_def.locate_card_object(card_name, board)
            human_gain += card_object.card_cost

        # how much does the AI care about these properties?
        for card_name in properties_offered:

            card_offered = c_def.locate_card_object(card_name, board)

            properties_valuation_personal += (money_offered-card_offered.card_cost) / card_offered.card_cost * multiplier

            # check if the AI already owns a property in that color group
            card_group = card_offered.color_group
            num_properties_in_group = 0

            for card in ai.cards_owned:
                if card.color_group == card_group:
                    num_properties_in_group += 1

            benefit += 10 + (10 * num_properties_in_group)

        for card_name in properties_wanted:

            card_wanted = c_def.locate_card_object(card_name, board)

            # check if the AI already owns a property in that color group

            card_group = card_wanted.color_group
            num_properties_in_group = 0

            for card in ai.cards_owned:
                if card.color_group == card_group:
                    num_properties_in_group += 1

            benefit -= 40 + (num_properties_in_group * 10)

    # evaluate money exchange
    personal_gain += (money_offered - money_wanted) * multiplier/10

    # cost/benefit analysis:
    print(f"Personal gain: {personal_gain}. Human gain: {human_gain}")
    if personal_gain > human_gain + 10:
        return 1
    else:
        return 0

