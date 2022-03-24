import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().strip().split())
tomatoes = [[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)] for _ in range(h)]

dz = [1, -1]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

cnt = 0
q = deque()
nq = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatoes[i][j][k] == 1:
                q.append([i, j, k])
                cnt += 1
            if tomatoes[i][j][k] == -1:
                cnt += 1

day = 0

while q:
    z, y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if tomatoes[z][ny][nx] == 0:
                tomatoes[z][ny][nx] = 1
                nq.append([z, ny, nx])
                cnt += 1

    for i in range(2):
        nz = z + dz[i]
        if 0 <= nz < h:
            if tomatoes[nz][y][x] == 0:
                tomatoes[nz][y][x] = 1
                nq.append([nz, y, x])
                cnt += 1
    
    if not q and nq:
        q = nq
        nq = deque()
        day += 1

if cnt == h * n * m:
    print(day)
else:
    print(-1)
