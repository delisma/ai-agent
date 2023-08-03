# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('---------')
    for i in range(3):
        print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')
        print('---------')

# Function to check if a player has won
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to play the game
def play_game():
    current_player = 'X'
    while True:
        print_board()
        position = input("Enter position (1-9): ")
        
        # Check if the input is a valid number
        if not position.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        
        position = int(position) - 1
        
        # Check if the input is within the valid range
        if position < 0 or position >= 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        # Check if the selected position is already occupied
        if board[position] != ' ':
            print("Invalid move. Position already occupied. Try again.")
            continue
        
        board[position] = current_player
        
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif ' ' not in board:
            print_board()
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
