import math
def solution(board):
    answer = board[0][0]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if i == 0 or j == 0:
                continue
            if board[i][j] == 1:
                answer = max(answer, width(board, i, j))

    return answer

def width(board, r, c):
    n = int(math.sqrt(min(board[r-1][c-1],board[r-1][c], board[r][c-1])))+1
    board[r][c] = n**2
    return n**2

board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
print(solution(board))
