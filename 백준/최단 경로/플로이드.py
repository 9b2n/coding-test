import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
buses = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n+1):
    buses[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    buses[a][b] = min(buses[a][b], c)

# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            buses[i][j] = min(buses[i][j], buses[i][k]+buses[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(0 if buses[i][j] == float('inf') else buses[i][j], end=' ')
    print()
