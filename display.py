# Function to print the board
def print_board(board):
    print('---------')
    for i in range(3):
        print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')
        print('---------')

# Function to get user input for position
def get_user_input():
    position = input("Enter position (1-9): ")
    return position
