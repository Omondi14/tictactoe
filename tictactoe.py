import random
import time

# Setup variables
occupied = set()
user_occupied = set()
comp_occupied = set()
win_list = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
endgame = False
play_choices = {"X", "O"}
board = ["_" for i in range(9)]
how_to_play_board = [i for i in range(9)]
intro_string = """
               Welcome to Ernie's TIC TAC TOE!!
               Play against the computer in this wonderful
               game that has all the joy of childhood while
               pitting you against our intelligent Computer
               player that will give you a run for your money!!!
               """

# Helper functions
def print_board(board):
    """
    Function takes a board and prints it in a spaced way
    """
    list_of_lists = [board[i:i+3] for i in range(0, len(board), 3)]
    for row in list_of_lists:
        print(*row)


def check_endgame(user_symbol, user_occupied, comp_symbol, comp_occupied):
    """
    Function that checks if the game is over and someone has won.
    Returns a boolean-string tuple:
        ("_" , False) -> No one has won and the game can continue
        ("X/O", True) -> "X/O" has won
    """
    winner_found = False
    # Loop through win list and see if user has won
    for win_set in win_list:
        if not winner_found and win_set.issubset(user_occupied):
            winner_found = True
            return (user_symbol, True)
        if not winner_found and win_set.issubset(comp_occupied):
            winner_found = True
            return (comp_symbol, True)
    if not winner_found:
        return ("_", False)

def random_comp_play(comp_symbol, board, occupied):
    """
    Function that chooses a position on the board for the Computer
    to play randomly.
    Input: comp_symbol: "X" or "O"
           board: dict with last play.
           occupied: set of occupied positions
    Return: board - with change reflecting computer play
    """
    playable_options = [item for item in range(9) if item not in occupied]
    comp_play = random.choice(playable_options)
    board[comp_play] = comp_symbol
    occupied.add(comp_play)
    comp_occupied.add(comp_play)
    return board


print(intro_string)
time.sleep(2)


# Choose symbol to play with
while True:
    user_symbol = input("""
                      Pick your symbol
                      Remember 'X' plays first.
                      'X' or 'O'? : """).capitalize()

    if user_symbol in play_choices:
        # Boolean that determines if user plays first
        user_play_first = True if user_symbol == "X" else False
        # Symbol that computer plays
        comp_symbol = "X" if not user_play_first else "O"
        # Get out of infinite loop
        break

how_to_play_str = f"""
                  Get ready to play.
                  Choose where to place '{user_symbol}' on the board based
                  on the following numbers.
                  """
time.sleep(2)
print(how_to_play_str)
# print board with numbers
time.sleep(2)
print_board(how_to_play_board)
print("")
time.sleep(2)

if user_play_first:
    # Run until game ends
    while True:
        # User's turn
        print("Your Turn!")
        print("")
        print_board(board)
        print("")
        time.sleep(2)
        # Loop to ensure user only picks unoccupied positions
        while True:
            print("Play by choosing one of the following positions")
            print_board(how_to_play_board)
            time.sleep(2)
            user_play = int(input("Choose unoccupied position to play: "))
            if user_play not in occupied:
                break
        board[user_play] = user_symbol
        occupied.add(user_play)
        user_occupied.add(user_play)
        time.sleep(2)
        print("You played!")
        print("")
        time.sleep(1)
        print_board(board)
        print("")

        # Check if game has ended
        end = check_endgame(user_symbol, user_occupied, comp_symbol, comp_occupied)
        if end[1]:
            break

        # Computer's turn
        print("Computer's Turn!")
        print("")
        print_board(board)
        print("")
        time.sleep(2)
        new_board = random_comp_play(comp_symbol, board, occupied)
        print("Computer played!")
        print("")
        time.sleep(1)
        print_board(new_board)

        # Check if game has ended
        end = check_endgame(user_symbol, user_occupied, comp_symbol, comp_occupied)
        if end[1]:
            break

    # Game has ended
    if end[0] == comp_symbol:
        comp_end_string = """
                          :(
                          YOU LOST!!! Better luck next time!
                          """
        time.sleep(2)
        print(comp_end_string)
    elif end[0] == user_symbol:
        user_end_string = """
                          :)
                          YOU WON!!!!! DO WE HAVE THE NEXT EINSTEIN? :D
                          """
        time.sleep(2)
        print(user_end_string)
else:
    # Computer plays first
    # Run until game ends
    while True:
        # Computer's turn
        print("Computer's Turn!")
        time.sleep(2)
        new_board = random_comp_play(comp_symbol, board, occupied)
        print("Computer played!")
        time.sleep(1)
        print_board(new_board)

        # Check if game has ended
        end = check_endgame(user_symbol, user_occupied, comp_symbol, comp_occupied)
        if end[1]:
            break

        # User's turn
        print("Your Turn!")
        print("")
        print_board(board)
        print("")
        time.sleep(2)
        # Loop to ensure user only picks unoccupied positions
        while True:
            print("Play by choosing one of the following positions")
            print_board(how_to_play_board)
            time.sleep(2)
            user_play = int(input("Choose unoccupied position to play: "))
            if user_play not in occupied:
                break
        board[user_play] = user_symbol
        occupied.add(user_play)
        user_occupied.add(user_play)
        time.sleep(2)
        print("You played!")
        print("")
        time.sleep(1)
        print_board(board)
        print("")

        # Check if game has ended
        end = check_endgame(user_symbol, user_occupied, comp_symbol, comp_occupied)
        if end[1]:
            break

    # Game has ended
    if end[0] == comp_symbol:
        comp_end_string = """
                          :(
                          YOU LOST!!! Better luck next time!
                          """
        time.sleep(2)
        print(comp_end_string)
    else:
        user_end_string = """
                          :)
                          YOU WON!!!!! DO WE HAVE THE NEXT EINSTEIN? :D
                          """
        time.sleep(2)
        print(user_end_string)
