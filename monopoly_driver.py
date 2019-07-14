"""
@author: Aleph Aseffa
Date created: 7/14/2019



"""


import class_definitions as cd
from information import brd


print("Beginning game!")
Aleph = cd.Player("Aleph", 1500, [], 0, False, 0)
Yah = cd.Player("Yah", 1500, [], 0, False, 0)

for i in range(3):
    print()
    print(f"Move {i+1}")
    dice_result = Aleph.roll_dice()
    Aleph.move_player(dice_result)
    Aleph.check_pos(brd)
    dice_result = Yah.roll_dice()
    Yah.move_player(dice_result)
    Yah.check_pos(brd)
