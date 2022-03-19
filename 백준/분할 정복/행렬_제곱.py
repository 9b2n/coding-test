n, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

def power(A, e):
    if e == 1:
        return A
    p = power(A, e//2)
    if e % 2:
        return mulMatrix(mulMatrix(p, p), A)
    return mulMatrix(p, p)

def mulMatrix(A, B):
    global n
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][k] += A[i][j]*B[j][k]
            C[i][k] %= 1000
    return C

result = power(A, b)

for i in range(n):
    for j in range(n):
        print(result[i][j]%1000, end=' ')
    print()
