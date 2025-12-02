"""Simple Tic Tac Toe Game.

A basic two-player Tic Tac Toe game played in the terminal.
Players alternate turns by selecting board positions.

Features:
- Dictionary-based board representation
- 9 positions labeled by location (e.g., 'top-L', 'mid-M')
- Turn-based gameplay for X and O
- Visual board display after each move

Note: This version does not include win condition checking.
"""

# Initialize the game board with empty spaces
theBoard = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": " ",
}


def printBoard(board):
    """
    Display the current state of the Tic Tac Toe board.
    
    Args:
        board (dict): Dictionary containing the board state with position keys.
    """
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


# Start with X as the first player
turn = "X"

# Main game loop - 9 turns for a complete game
for i in range(9):
    printBoard(theBoard)
    print("Turn for " + turn + ". Move on which space?")
    print(list(theBoard.keys()))  # Show available positions
    move = input()
    theBoard[move] = turn  # Place the player's marker
    
    # Switch turns between X and O
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

# Display final board state
printBoard(theBoard)
