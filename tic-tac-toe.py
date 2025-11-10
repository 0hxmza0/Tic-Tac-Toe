import random

# Display the current board
def display_board(board):
    for i in range(3):
        print(" {} | {} | {} ".format(board[i][0], board[i][1], board[i][2]))
        if i < 2:
            print("---+---+---")
    print()
# Let a player make a move
def player_choice(board, symbol):
    valid = False
    while not valid:
        choice = input(f"{symbol}'s turn. Enter a number between 1-9: ").strip()
        
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 9:
                row = (choice - 1) // 3
                col = (choice - 1) % 3
                if board[row][col] == ' ':
                    board[row][col] = symbol
                    valid = True
                else:
                    print("That cell is already taken. Try again.\n")
            else:
                print("Invalid number. Choose between 1-9.\n")
        else:
            print("Invalid input. Enter a number.\n")

# Check if a player has won
def check_win(board, symbol):
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2-i] == symbol for i in range(3)):
        return True
    return False

# Check if the board is full (draw)
def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Main game function
def main():
    # Initialize empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    # Randomly choose first player
    current_player = random.choice(["X", "O"])
    print(f"{current_player} goes first!\n")
    
    game_over = False
    
    while not game_over:
        display_board(board)  # Show board before each move
        player_choice(board, current_player)  # Current player makes a move
        display_board(board)  # Show updated board after move
        
        # Check for win
        if check_win(board, current_player):
            print(f"{current_player} wins!")
            game_over = True
            continue
        
        # Check for draw
        if check_draw(board):
            print("It's a draw!")
            game_over = True
            continue
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    main()
