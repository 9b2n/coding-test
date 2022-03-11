n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
w, b = 0, 0

def repetition(arr, x, y, m):
    global w, b
    s = isFull(arr, x, y, m)
    if s == 0:
        w += 1
        return
    elif s == m**2:
        b += 1
        return
    else:
        l = m//2
        repetition(arr, x, y, l)
        repetition(arr, x+l, y, l)
        repetition(arr, x, y+l, l)
        repetition(arr, x+l, y+l, l)


def isFull(arr, x, y, m):
    s = 0
    for i in range(m):
        for j in range(m):
            s += arr[y+i][x+j]
    return s

repetition(paper, 0, 0, n)
print(w)
print(b)
