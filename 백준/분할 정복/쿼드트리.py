n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
result = []

def quadTree(y,x,n):
    global result
    compare = arr[y][x]

    for i in range(y, y+n):
        for j in range(x, x+n):
            if compare != arr[i][j]:
                result.append("(")
                quadTree(y,x,n//2)
                quadTree(y, x+n//2, n//2)
                quadTree(y+n//2, x, n//2)
                quadTree(y+n//2, x+n//2, n//2)
                result.append(")")
                return
    result.append(compare)

quadTree(0,0,n)
print("".join(map(str,(result))))
