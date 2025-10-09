import random

rows, cols = 9, 9
mines = 10


board = [[0 for _ in range(cols)] for _ in range(rows)]
userBoard = [[None for _ in range(cols)] for _ in range(rows)]

def printBoard(b):
    # Print column headers
    print("   " + " ".join(str(c) for c in range(cols)))
    print("  " + "--" * cols)
    for r in range(rows):
        line = []
        for c in range(cols):
            v = b[r][c]
            line.append('?' if v is None else str(v))
        # Print row index + row contents
        print(f"{r} | " + " ".join(line))


def place_mines():
    placed = 0
    while placed < mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if board[r][c] != 'x':
            board[r][c] = 'x'
            placed += 1

def count_neighbors(r, c):
    if board[r][c] == 'x':
        return -1
    cnt = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'x':
                cnt += 1
    return cnt

def compute_numbers():
    for r in range(rows):
        for c in range(cols):
            if board[r][c] != 'x':
                cnt = count_neighbors(r, c)
                board[r][c] = 0 if cnt < 0 else cnt

def revealSurroundingSquares(r, c):
    # bounds
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    # already revealed
    if userBoard[r][c] is not None:
        return
    # don't reveal mines here
    if board[r][c] == 'x':
        return

    # reveal FIRST
    userBoard[r][c] = board[r][c]

    # expand only if it's a zero
    if board[r][c] != 0:
        return

    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            revealSurroundingSquares(r + dr, c + dc)

def getUserInput():
    print()
    x = int(input("Enter row (0-8): "))
    y = int(input("Enter col (0-8): "))
    print()
    if board[x][y] == 'x':
        print()
        print("Game over")
        print()
        printBoard(board)
        return False
    revealSurroundingSquares(x, y)
    return True

def winCheck(userBoard) -> bool:
     for r in range(rows):
        for c in range(cols):
            if board[r][c] != 'x' and userBoard[r][c] == '?':
                return False
     return True
    
place_mines()
compute_numbers()


printBoard(userBoard)

while(getUserInput() != False):
    printBoard(userBoard)
    winCheck(userBoard)
