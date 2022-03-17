n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
minus, zero, plus = 0, 0, 0

def divideNConquer(arr, y, x, n):
    global minus, zero, plus
    compare = arr[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if arr[i][j] != compare:
                for row in range(3):
                    for col in range(3):
                        divideNConquer(arr, y+n//3*row, x+n//3*col, n//3)
                return
    if compare == -1:
        minus += 1
    elif compare == 0:
        zero += 1
    else:
        plus += 1
    

divideNConquer(paper, 0, 0, n)
print(minus)
print(zero)
print(plus)
