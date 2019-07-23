"""
@author: Aleph Aseffa
Date created: 7/14/2019

This file contains all the base information needed for the game to work.
This includes:
    - Board details
    - Community chest information
    - Chance information
"""
import card_definitions as c_def

# card_name, color_group, card_cost, house_cost, houses_built, rent_prices, mortgage_amt, owner, mortgaged


def initialize_cards_and_board():
    """
    Creates all the needed card objects and adds them in the correct order to the board variable.
    The board represents the order of cards in the original Monopoly game board.
    :return: board: a list of cards.
    """
    go = c_def.Card("Go", "N/A", 0, 0, 0, {}, 0, "Bank", False)
    med_ave = c_def.Card("Mediterranean Avenue", "Brown", 60, 0, 0, {1: 100}, 0, "Bank", False)
    comm_chest = c_def.Card("Community Chest", "N/A", 0, 0, 0, {1: 100}, 0, "Bank", False)
    baltic_ave = c_def.Card("Baltic Avenue", "Brown", 60, 0, 0, {1: 100}, 0, "Bank", False)
    income_tax = c_def.Card("Income Tax", "N/A", 200, 0, 0, {1: 100}, 0, "Bank", False)
    reading_rr = c_def.Card("Reading Railroad", "Railroad", 200, 0, 0, {1: 100}, 0, "Bank", False)
    oriental_ave = c_def.Card("Oriental Avenue", "Light Blue", 100, 0, 0, {1: 100}, 0, "Bank", False)
    chance = c_def.Card("Community Chest", "N/A", 0, 0, 0, {1: 100}, 0, "Bank", False)
    vermont_ave = c_def.Card("Vermont Avenue", "Light Blue", 100, 0, 0, {1: 100}, 0, "Bank", False)
    conn_ave = c_def.Card("Connecticut Avenue", "Light Blue", 120, 0, 0, {1: 100}, 0, "Bank", False)

    jail = c_def.Card("Jail/Visiting Jail", "N/A", 0, 0, 0, {1: 100}, 0, "Bank", False)
    st_charles_place = c_def.Card("St. Charles Place", "Pink", 140, 0, 0, {1: 100}, 0, "Bank", False)
    electric_company = c_def.Card("Electric Company", "Utilities", 150, 0, 0, {1: 100}, 0, "Bank", False)
    states_ave = c_def.Card("States Avenue", "Pink", 140, 0, 0, {1: 100}, 0, "Bank", False)
    virginia_ave = c_def.Card("Virginia Avenue", "Pink", 160, 0, 0, {1: 100}, 0, "Bank", False)
    penn_rr = c_def.Card("Pennsylvania Railroad", "Railroad", 200, 0, 0, {1: 100}, 0, "Bank", False)
    st_james_place = c_def.Card("St. James Place", "Orange", 180, 0, 0, {1: 100}, 0, "Bank", False)
    # comm chest
    ten_ave = c_def.Card("Tennessee Avenue", "Orange", 180, 0, 0, {1: 100}, 0, "Bank", False)
    ny_ave = c_def.Card("New York Avenue", "Orange", 200, 0, 0, {1: 100}, 0, "Bank", False)
    free_parking = c_def.Card("Free Parking", "N/A", 0, 0, 0, {1: 100}, 0, "Bank", False)

    kentucky_ave = c_def.Card("Kentucky Avenue", "Red", 220, 0, 0, {1: 100}, 0, "Bank", False)
    # chance
    indiana_ave = c_def.Card("Indiana Avenue", "Red", 220, 0, 0, {1: 100}, 0, "Bank", False)
    illinois_ave = c_def.Card("Illinois Avenue", "Red", 240, 0, 0, {1: 100}, 0, "Bank", False)
    bno_rr = c_def.Card("B. & O. Railroad", "Railroad", 200, 0, 0, {1: 100}, 0, "Bank", False)
    atlantic_ave = c_def.Card("Atlantic Avenue", "Yellow", 260, 0, 0, {1: 100}, 0, "Bank", False)
    ventnor_ave = c_def.Card("Ventnor Avenue", "Yellow", 260, 0, 0, {1: 100}, 0, "Bank", False)
    water_works = c_def.Card("Water Works", "Utilities", 150, 0, 0, {1: 100}, 0, "Bank", False)
    marvin_gardens = c_def.Card("Marvin Gardens", "Yellow", 280, 0, 0, {1: 100}, 0, "Bank", False)

    go_to_jail = c_def.Card("Go to Jail", "N/A", 0, 0, 0, {1: 100}, 0, "Bank", False)
    pacific_ave = c_def.Card("Pacific Avenue", "Green", 300, 0, 0, {1: 100}, 0, "Bank", False)
    nc_ave = c_def.Card("North Carolina Avenue", "Green", 140, 0, 0, {1: 100}, 0, "Bank", False)
    # comm chest
    penn_ave = c_def.Card("Pennsylvania Avenue", "Green", 300, 0, 0, {1: 100}, 0, "Bank", False)
    short_line_rr = c_def.Card("Short Line", "Railroad", 200, 0, 0, {1: 100}, 0, "Bank", False)
    # chance
    park_place = c_def.Card("Park Place", "Blue", 350, 0, 0, {1: 100}, 0, "Bank", False)
    luxury_tax = c_def.Card("Luxury Tax", "N/A", 100, 0, 0, {1: 100}, 0, "Bank", False)
    boardwalk = c_def.Card("Boardwalk", "N/A", 400, 0, 0, {1: 100}, 0, "Bank", False)

    board = [
        go,
        med_ave,
        comm_chest,
        baltic_ave,
        income_tax,
        reading_rr,
        oriental_ave,
        chance,
        vermont_ave,
        conn_ave,
        jail,
        st_charles_place,
        electric_company,
        states_ave,
        virginia_ave,
        penn_rr,
        st_james_place,
        comm_chest,
        ten_ave,
        ny_ave,
        free_parking,
        kentucky_ave,
        chance,
        indiana_ave,
        illinois_ave,
        bno_rr,
        atlantic_ave,
        ventnor_ave,
        water_works,
        marvin_gardens,
        go_to_jail,
        pacific_ave,
        nc_ave,
        comm_chest,
        penn_ave,
        short_line_rr,
        chance,
        park_place,
        luxury_tax,
        boardwalk
    ]

    return board


def display_instructions() -> None:
    """
    Displays possible options for players.
    :return: None
    """
    print("Instruction.......................................Command")
    print("Roll dice...........................................r")
    print("View balance........................................b")
    print("View cards and houses owned.........................c")
    print("Sell property.......................................s")
    print("Mortgage property...................................m")
    print("Construct house.....................................h")

