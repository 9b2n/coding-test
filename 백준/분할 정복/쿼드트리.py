n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
result = []

def quadTree(y,x,n):
    compare = arr[y][x]

    for i in range(y, y+n):
        for j in range(x, x+n):
            if compare != arr[i][j]:
                result.append("(")
                for row in range(2):
                    for col in range(2):
                        quadTree(y+n//2*row, x+n//2*col, n//2)
                result.append(")")
                return
    result.append(compare)

quadTree(0,0,n)
print("".join(map(str,(result))))
