
def print_board():
    for i in range(0, 3):
        current_row = ""
        for j in range(0, 3):
            if board[i][j] == "e":
                current_row += "_  "
            else:
                current_row += board[i][j] + "  "
        print(current_row)
        # print("\n")


def check_winner(row, column):
    win = False
    current_piece = board[row][column]
    num_in_a_row = 1
    # check row

    current_column = column - 1
    while current_column >= 0:
        if board[row][current_column] == current_piece:
            num_in_a_row += 1
        current_column -= 1

    current_column = column + 1
    while current_column < 3:
        if board[row][current_column] == current_piece:
            num_in_a_row += 1
        current_column += 1

    if num_in_a_row == 3:
        win = True
        return win

    # check column
    num_in_a_row = 1

    current_row = row - 1
    while current_row >= 0:
        if board[current_row][column] == current_piece:
            num_in_a_row += 1
        current_row -= 1

    current_row = row + 1
    while current_row < 3:
        if board[current_row][column] == current_piece:
            num_in_a_row += 1
        current_row += 1

    if num_in_a_row == 3:
        win = True
        return win

    # check diagonal
    num_in_a_row = 1
    current_row = row - 1
    current_column = column - 1
    while current_row >= 0 and current_column >= 0:
        if board[current_row][current_column] == current_piece:
            num_in_a_row += 1
        current_row -= 1
        current_column -= 1

    current_row = row + 1
    current_column = column + 1
    while current_row < 3 and current_column < 3:
        if board[current_row][current_column] == current_piece:
            num_in_a_row += 1
        current_row += 1
        current_column += 1

    if num_in_a_row == 3:
        win = True
        return win

    return win


def check_draw():
    for row in board:
        for cell in row:
            if cell == "e":
                return False
    return True


# Initiate the board
# board = []
# for i in range(0, 3):
#     board.append(["e", "e", "e"])
m = 3
n = 3
board = [""] * m
for i in range(m):
    board[i] = ["e"] * n
print_board()
game_on = True

while game_on:
    row_1 = int(input("Player 1, type your row number (row number starts from 0): "))
    column_1 = int(input("Player 1, type your column number (column number starts from 0): "))
    while row_1 > 2 or row_1 < 0 or column_1 > 2 or column_1 < 0 or board[row_1][column_1] != "e":
        print("Invalid row or column number, try again!")
        row_1 = int(input("Player 1, type your row number (row number starts from 0): "))
        column_1 = int(input("Player 1, type your column number (column number starts from 0): "))

    board[row_1][column_1] = "x"
    print_board()
    if check_winner(row_1, column_1):
        game_on = False
        print("Player 1 wins!")
        break
    if check_draw():
        game_on = False
        print("It's a draw!")
        break

    row_2 = int(input("Player 2, type your row number (row number starts from 0): "))
    column_2 = int(input("Player 2, type your column number (column number starts from 0): "))
    while row_2 > 2 or row_2 < 0 or column_2 > 2 or column_2 < 0 or board[row_2][column_2] != "e":
        print("Invalid row or column number, try again!")
        row_2 = int(input("Player 2, type your row number (row number starts from 0): "))
        column_2 = int(input("Player 2, type your column number (column number starts from 0): "))

    board[row_2][column_2] = "o"
    print_board()
    if check_winner(row_2, column_2):
        game_on = False
        print("Player 2 wins!")
        break
    if check_draw():
        game_on = False
        print("It's a draw!")
        break
