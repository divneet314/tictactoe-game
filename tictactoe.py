def printboard(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def checkwinner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True
    return False

def isboardfull(board):
    return all(board[i][j] != "" for i in range(3) for j in range(3))

def getmove():
    while True:
        try:
            row = int(input("enter the row (0, 1, or 2):"))
            col = int(input("enter the column (0, 1, or 2):"))
            if 0 <= row < 3 and 0 <= col < 3:
                return row, col
            else:
                print("invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("invalid input. Please enter valid integers.")

def tic_tac_toe():
    board = [["" for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_idx = 0
    while not isboardfull(board):
        current_player = players[player_idx]
        printboard(board)
        print(f"Player {current_player}'s turn.")
        row, col = getmove()
        if board[row][col] == "":
            board[row][col] = current_player
            if checkwinner(board, current_player):
                printboard(board)
                print(f"Player {current_player} wins!")
                break
            player_idx = 1 - player_idx
        else:
            print("That cell is already occupied. Try again.")
    else:
        printboard(board)
        print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
