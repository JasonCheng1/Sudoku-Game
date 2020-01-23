
board = [[5, 3, 0,   0, 7, 0,   0, 0, 0],
         [6, 0, 0,   1, 9, 5,   0, 0, 0],
         [0, 9, 8,   0, 0, 0,   0, 6, 0],

         [8, 0, 0,   0, 6, 0,   0, 0, 3],
         [4, 0, 0,   8, 0, 3,   0, 0, 1],
         [7, 0, 0,   0, 2, 0,   0, 0, 6],

         [0, 6, 0,   0, 0, 0,   2, 8, 0],
         [0, 0, 0,   4, 1, 9,   0, 0, 5],
         [0, 0, 0,   0, 8, 0,   0, 7, 9]]


def print_board(board: [[int]]) -> None:
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("_______________________")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    print("\n<_______________________>\n")


def find_blank(board: [[int]]) -> ():
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def valid(board, num, pos):
    return check_row(board, num, pos) and check_col(board, num, pos) and check_box(board, num, pos)


def check_row(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and i != pos[1]:
            return False
    return True


def check_col(board, num, pos):
    for i in range(len(board)):
        if board[i][pos[1]] == num and i != pos[0]:
            return False
    return True


def check_box(board, num, pos):
    x = pos[1]//3
    y = pos[0]//3
    for i in range(3*y, 3*y + 3):
        for j in range(3*x, 3*x + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def possible(board, pos) -> []:
    res = [0] * 10
    for i in range(len(board[0])):
        res[board[pos[0]][i]] += 1
    for i in range(len(board)):
        res[board[i][pos[1]]] += 1
    x = pos[1]//3
    y = pos[0]//3
    for i in range(3*y, 3*y + 3):
        for j in range(3*x, 3*x + 3):
            res[board[i][j]] += 1
    return res


def solve(board: [[int]]):
    pos = find_blank(board)
    if not pos:
        return True

    plausible = possible(board, pos)
    for i in range(1, 10):
        if plausible[i] == 0:
            if (valid(board, i, pos)):
                board[pos[0]][pos[1]] = i
                if(solve(board)):
                    return True
                board[pos[0]][pos[1]] = 0
    return False


print_board(board)
solve(board)
print_board(board)
