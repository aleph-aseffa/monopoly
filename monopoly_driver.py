"""
@author: Aleph Aseffa
Date created: 7/14/2019



"""

from classes import player_definitions as p_def
from game import information as info
from ai import ai

board = info.initialize_cards_and_board()

Aleph = p_def.Player("Aleph", 1500, [], 0, False, 0, 0, 0, False)
Yah = p_def.Player("Yah", 1500, [], 0, False, 0, 0, 0, False)
Computer = p_def.Player("AI", 1500, [], 0, False, 0, 0, 0, False)
player_list = [Aleph, Yah, Computer]


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
    print("Beginning game!")
    info.display_instructions()

    i = 0
    # continue running while there is more than one non-bankrupt player remaining.
    while count_bankrupt_players(player_list) != len(player_list)-1:
        i = i % len(player_list)

        print()
        print(f"{player_list[i].name}'s turn:")

        if player_list[i].name == "AI":
            ai.move(Computer)

        else:
            user_choice = input("What do you want to do? ")
            result = player_list[i].player_action(user_choice, player_list)
            while result == -1:  # keep asking the user until they choose to roll the dice.
                user_choice = input("What do you want to do? ")
                result = player_list[i].player_action(user_choice, player_list)
            new_pos = player_list[i].move_player(result)
            player_list[i].check_pos(board)

        i += 1

    print(f"Game over! {display_winner(player_list)} has won!")
