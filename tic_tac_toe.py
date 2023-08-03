from game_logic import check_win, make_move, is_board_full
from display import print_board, get_user_input

# Create the board
board = [' ' for _ in range(9)]

# Function to play the game
def play_game():
    current_player = 'X'
    while True:
        print_board(board)
        position = get_user_input()
        
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
        
        make_move(position, current_player)
        
        if check_win(current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full():
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
