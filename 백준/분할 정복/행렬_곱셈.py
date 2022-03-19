import sys

n, m = map(int, sys.stdin.readline().strip().split())
A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

m, l = map(int, sys.stdin.readline().strip().split())
B = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

C = [[0] * l for _ in range(n)]

for i in range(n):
    for k in range(l):
        for j in range(m):
            C[i][k] += A[i][j]*B[j][k]

for i in range(n):
    print(*C[i])
