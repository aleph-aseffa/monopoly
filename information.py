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
    go = c_def.Card("Go", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "Bank", False)
    med_ave = c_def.Card("Mediterranean Avenue", "Brown", 60, 50, 0, {0: 2,
                                                                      1: 10,
                                                                      2: 30,
                                                                      3: 90,
                                                                      4: 160,
                                                                      5: 250}, 30, "Bank", False)
    comm_chest = c_def.Card("Community Chest", "N/A", 0, 0, 0, "N/A", 0, "Bank", False)
    baltic_ave = c_def.Card("Baltic Avenue", "Brown", 60, 50, 0, {0: 4,
                                                                  1: 20,
                                                                  2: 60,
                                                                  3: 180,
                                                                  4: 320,
                                                                  5: 450}, 30, "Bank", False)
    income_tax = c_def.Card("Income Tax", "N/A", 200, 0, 0, {1: 100}, 0, "Bank", False)
    reading_rr = c_def.Card("Reading Railroad", "Railroad", 200, "N/A", "N/A", {1: 25}, 100, "Bank", False)
    oriental_ave = c_def.Card("Oriental Avenue", "Light Blue", 100, 50, 0, {0: 6,
                                                                            1: 30,
                                                                            2: 90,
                                                                            3: 270,
                                                                            4: 400,
                                                                            5: 550}, 50, "Bank", False)
    chance = c_def.Card("Community Chest", "N/A", 0, 0, 0, {1: 100}, 0, "Bank", False)
    vermont_ave = c_def.Card("Vermont Avenue", "Light Blue", 100, 50, 0, {0: 6,
                                                                          1: 30,
                                                                          2: 90,
                                                                          3: 270,
                                                                          4: 400,
                                                                          5: 550}, 50, "Bank", False)
    conn_ave = c_def.Card("Connecticut Avenue", "Light Blue", 120, 50, 0, {0: 8,
                                                                           1: 40,
                                                                           2: 100,
                                                                           3: 300,
                                                                           4: 450,
                                                                           5: 600}, 60, "Bank", False)
    # new row
    jail = c_def.Card("Jail/Visiting Jail", "N/A", 0, 0, 0, {1: 100}, 0, "Bank", False)
    st_charles_place = c_def.Card("St. Charles Place", "Pink", 140, 100, 0, {0: 10,
                                                                             1: 50,
                                                                             2: 150,
                                                                             3: 450,
                                                                             4: 625,
                                                                             5: 750}, 70, "Bank", False)
    electric_company = c_def.Card("Electric Company", "Utilities", 150, "N/A", "N/A", "N/A", 75, "Bank", False)
    states_ave = c_def.Card("States Avenue", "Pink", 140, 100, 0, {0: 10,
                                                                   1: 50,
                                                                   2: 150,
                                                                   3: 450,
                                                                   4: 625,
                                                                   5: 750}, 70, "Bank", False)
    virginia_ave = c_def.Card("Virginia Avenue", "Pink", 160, 100, 0, {0: 12,
                                                                       1: 60,
                                                                       2: 180,
                                                                       3: 500,
                                                                       4: 700,
                                                                       5: 900}, 80, "Bank", False)
    penn_rr = c_def.Card("Pennsylvania Railroad", "Railroad", 200, 0, 0, {1: 100}, 100, "Bank", False)
    st_james_place = c_def.Card("St. James Place", "Orange", 180, 100, 0, {0: 14,
                                                                           1: 70,
                                                                           2: 200,
                                                                           3: 550,
                                                                           4: 750,
                                                                           5: 950}, 90, "Bank", False)
    # comm chest
    ten_ave = c_def.Card("Tennessee Avenue", "Orange", 180, 100, 0, {0: 14,
                                                                     1: 70,
                                                                     2: 200,
                                                                     3: 550,
                                                                     4: 750,
                                                                     5: 950}, 90, "Bank", False)
    ny_ave = c_def.Card("New York Avenue", "Orange", 200, 100, 0, {0: 16,
                                                                   1: 80,
                                                                   2: 220,
                                                                   3: 600,
                                                                   4: 800,
                                                                   5: 1000}, 100, "Bank", False)
    free_parking = c_def.Card("Free Parking", "N/A", 0, 0, 0, {1: 100}, 0, "Bank", False)
    # rotate
    kentucky_ave = c_def.Card("Kentucky Avenue", "Red", 220, 150, 0, {0: 18,
                                                                      1: 90,
                                                                      2: 250,
                                                                      3: 700,
                                                                      4: 875,
                                                                      5: 1050}, 110, "Bank", False)
    # chance
    indiana_ave = c_def.Card("Indiana Avenue", "Red", 220, 150, 0, {0: 18,
                                                                    1: 90,
                                                                    2: 250,
                                                                    3: 700,
                                                                    4: 875,
                                                                    5: 1050}, 110, "Bank", False)
    illinois_ave = c_def.Card("Illinois Avenue", "Red", 240, 150, 0, {0: 20,
                                                                      1: 100,
                                                                      2: 300,
                                                                      3: 750,
                                                                      4: 925,
                                                                      5: 1100}, 120, "Bank", False)
    bno_rr = c_def.Card("B. & O. Railroad", "Railroad", 200, 0, 0, {1: 100}, 100, "Bank", False)
    atlantic_ave = c_def.Card("Atlantic Avenue", "Yellow", 260, 150, 0, {0: 22,
                                                                         1: 110,
                                                                         2: 330,
                                                                         3: 800,
                                                                         4: 975,
                                                                         5: 1150}, 130, "Bank", False)
    ventnor_ave = c_def.Card("Ventnor Avenue", "Yellow", 260, 150, 0, {0: 22,
                                                                       1: 110,
                                                                       2: 330,
                                                                       3: 800,
                                                                       4: 975,
                                                                       5: 1150}, 130, "Bank", False)
    water_works = c_def.Card("Water Works", "Utilities", 150, 0, 0, {1: 100}, 75, "Bank", False)
    marvin_gardens = c_def.Card("Marvin Gardens", "Yellow", 280, 150, 0, {0: 24,
                                                                          1: 120,
                                                                          2: 360,
                                                                          3: 850,
                                                                          4: 1025,
                                                                          5: 1200}, 140, "Bank", False)
    # rotate
    go_to_jail = c_def.Card("Go to Jail", "N/A", 0, 0, 0, {1: 100}, 0, "Bank", False)
    pacific_ave = c_def.Card("Pacific Avenue", "Green", 300, 200, 0, {0: 26,
                                                                      1: 130,
                                                                      2: 390,
                                                                      3: 900,
                                                                      4: 1100,
                                                                      5: 1275}, 150, "Bank", False)
    nc_ave = c_def.Card("North Carolina Avenue", "Green", 140, 200, 0, {0: 26,
                                                                        1: 130,
                                                                        2: 390,
                                                                        3: 900,
                                                                        4: 1100,
                                                                        5: 1275}, 150, "Bank", False)
    # comm chest
    penn_ave = c_def.Card("Pennsylvania Avenue", "Green", 300, 200, 0, {0: 28,
                                                                        1: 150,
                                                                        2: 450,
                                                                        3: 1000,
                                                                        4: 1200,
                                                                        5: 1400}, 160, "Bank", False)
    short_line_rr = c_def.Card("Short Line", "Railroad", 200, 0, 0, {1: 100}, 100, "Bank", False)
    # chance
    park_place = c_def.Card("Park Place", "Blue", 350, 200, 0, {0: 35,
                                                                1: 175,
                                                                2: 500,
                                                                3: 1100,
                                                                4: 1300,
                                                                5: 1500}, 175, "Bank", False)
    luxury_tax = c_def.Card("Luxury Tax", "N/A", 100, 0, 0, {1: 100}, 0, "Bank", False)
    boardwalk = c_def.Card("Boardwalk", "N/A", 400, 200, 0, {0: 50,
                                                             1: 200,
                                                             2: 600,
                                                             3: 1400,
                                                             4: 1700,
                                                             5: 2000}, 200, "Bank", False)
    # end
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

