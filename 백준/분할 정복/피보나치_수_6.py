n = int(input())
m = 1000000007
def power(F, e):
    if e == 1:
        return [[1, 1], [1, 0]]
    p = power(F, e // 2)
    if e % 2:
        return mul(mul(p, p), F)
    return mul(p, p)

def mul(A, B):
    global m
    C = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for k in range(len(B[0])):
            for j in range(len(B)):
                C[i][k] += A[i][j]*B[j][k]
            C[i][k] %= m
    return C

print(mul(power([[1, 1], [1, 0]], n-2), [[1],[1]])[0][0]%m)
