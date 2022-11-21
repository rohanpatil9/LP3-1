
N = int(input("Enter the number of Queens: "))
board = [[0] * N for _ in range(N)]

def isNotSafe(i, j):
    for k in range(N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
        for l in range(N):
            if (k+l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False


def placeNQueens(n):
    if n == 0:
        return True

    for i in range(N):
        for j in range(N):
            if (not(isNotSafe(i, j)) and board[i][j] != 1):
                board[i][j] = 1

                if placeNQueens(n - 1) == True:
                    return True

                board[i][j] = 0

    return False

placeNQueens(N)

for i in board:
    print(i)
