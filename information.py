"""
@author: Aleph Aseffa
Date created: 7/14/2019

This file contains all the base information needed for the game to work.
This includes:
    - Board details
    - Community chest information
    - Chance information
"""

import class_definitions as cd

# def __init__(self, card_name, color_group, card_cost, house_cost, rent_prices, mortgage_amt, owner, mortgaged):

board_array = ["Park Place", "Community Chest", "Chance", "Ventnor Avenue", "Go to Jail"]

# definitions of cards:
park_place = cd.Card("Park Place", "Blue", 350, 50, ["something"], 175, "Bank", False)
comm_chest = cd.Card("Community Chest", "N/A", 0, 0, ["something"], 0, "Bank", False)
chance = cd.Card("Chance", "N/A", 350, 50, ["something"], 175, "Bank", False)
ventnor_ave = cd.Card("Ventnor Avenue", "Yellow", 350, 50, ["something"], 175, "Bank", False)
go_to_jail = cd.Card("Go to Jail", "N/A", 350, 50, ["something"], 175, "Bank", False)

brd = [park_place, comm_chest, chance, ventnor_ave, go_to_jail]
