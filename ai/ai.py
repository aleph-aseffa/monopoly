"""
Contains the code for the AI that can play against the user.
"""
from monopoly_driver import board


def move(ai):

    if ai.in_jail:
        leave_jail(ai)

    dice_roll = ai.roll_dice()
    ai.move_player(dice_roll)
    curr_card = board[ai.current_pos % 40]
    purchasable = ai.check_pos(board)

    if purchasable and ai.balance > curr_card.card_cost:
        curr_card.purchase_card(ai)
        print(f"{ai.name} has purchased {curr_card.card_name}")


def leave_jail(ai):
    ai.reduce_balance(50)
    ai.in_jail = False
    print(f"{ai.name} has paid the $50 bail and has been released from jail.")
    move(ai)


def evaluate_trade(human, money, properties):  # TODO: finish function
    pass

