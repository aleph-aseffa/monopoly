"""
@author: Aleph Aseffa
Date created: 7/14/2019



"""


import class_definitions as cd
import information as info


print("Beginning game!")
info.display_instructions()
board = info.initialize_cards_and_board()

Aleph = cd.Player("Aleph", 1500, [], 0, False, 0, 0, 0, False)
Yah = cd.Player("Yah", 50, [], 0, False, 0, 0, 0, False)
player_list = [Aleph, Yah]


def count_bankrupt_players(players):
    """
    Counts how many players have been bankrupted.
    :param players: list, players that are playing the game.
    :return: int, number of players that are bankrupt.
    """
    counter = 0
    for player in players:
        if player.bankruptcy_status:
            counter += 1
    return counter


def display_winner(players):
    """
    Prints out which player has won.
    :param players: list, players that are playing the game.
    :return: None.
    """
    for player in players:
        if player.bankruptcy_status == False:
            return player.name


if __name__ == "__main__":
    i = 0
    # continue running while there is more than one non-bankrupt player remaining.
    while count_bankrupt_players(player_list) != len(player_list)-1:
        i = i % len(player_list)
        print()
        print(f"Move {i+1}")

        print(f"{player_list[i].name}'s turn:")
        user_choice = input("What do you want to do? ")
        result = player_list[i].player_action(user_choice)

        while result == -1:  # keep asking the user until they choose to roll the dice.
            user_choice = input("What do you want to do? ")
            result = player_list[i].player_action(user_choice)

        new_pos = player_list[i].move_player(result)
        player_list[i].check_pos(board)
        i += 1

    print(f"Game over! {display_winner(player_list)} has won!")
