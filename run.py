#
#Code written is inspired by the Youtube channel Knowledge Mavens- 'How to Code Battleship in Python'
#Code adjusted by the developer to better fit this specific gameboard
#

from random import randint

#
# General symbols used on gameboard
# X for placing ship and hit battleship
# " " for available space
# "-" for missed shot
#

#Hidden board for holding computer ship locations (board is 7 x 7 squares)
HIDDEN_BOARD = [[" "] * 7 for x in range(7)]
# Visible board for displaying hits and misses (board is 7 x 7 squares)
USER_BOARD = [[" "] * 7 for x in range(7)]

#variable to convert letters to numbers
letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}

def print_board(board):
    """
    Function to create the visual set up of the board
    """
    print("  A B C D E F G")
    print("  +-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def generate_ships(board):
    """
    Function for computer to generate 5 random ships on hidden board.
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,6), randint(0,6)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = find_ship_location()
        board[ship_row][ship_column] = "X"


def find_ship_location():
    """
    Function for user input to select row and column incl explanatory text.
    """
    row = input("Please enter a row between 1-7: ")
    while row not in "1234567":
        print("Wrong, please enter a valid row")
        row = input("Please enter a row between 1-7: ")
    column = input("Please enter a column between A-G: ").upper()
    while column not in "ABCDEFG":
        print("Wrong, please select a valid column")
        column = input("Please enter a column between A-G: ").upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):
    """
    Function to check if ships are hit and return count plus increment count
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


generate_ships(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print("Find the battle ship locations")
    print_board(USER_BOARD)
    row, column = find_ship_location()
    if USER_BOARD[row][column] == "-":
        print("You've already guessed that")
    elif HIDDEN_BOARD[row][column] == "X":
        print("It's a HIT!")
        USER_BOARD[row][column] = "X" 
        turns -= 1  
    else:
        print("It's a MISS!")
        USER_BOARD[row][column] = "-"   
        turns -= 1     
    if count_hit_ships(USER_BOARD) == 4:
        print("Congratulations! You hit 4 ships and won the game!")
        break
    print("You have " + str(turns) + " turns remaining")
    if turns == 0:
        print("Game Over, you've run out of turns!")
        break
