import sys
from collections import deque

t = int(input())
for _ in range(t):

    m, n, k = map(int, sys.stdin.readline().strip().split())
    farm = [[0] * m for _ in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        farm[y][x] = 1

    for i in range(n):
        for j in range(m):
            if farm[i][j] == 0 or farm[i][j] > 1:
                continue
            q = deque()
            q.append([i, j])
            farm[i][j] += 1
            cnt += 1
            while q:
                y, x = q.popleft()
                
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < m and 0 <= ny < n:
                        if farm[ny][nx] == 1:
                            farm[ny][nx] += 1
                            q.append([ny, nx])
    
    print(cnt)
