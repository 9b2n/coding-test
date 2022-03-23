import sys
from collections import deque

m, n = map(int, sys.stdin.readline().strip().split())
box = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
tomatoes = deque()
cells = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tomatoes.append([i, j])
            cells += 1
        if box[i][j] == -1:
            cells += 1

day = 0
q = deque()
nq = deque()
for py, px in tomatoes:
    q.append([py, px])

while q:
    y, x = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if box[ny][nx] == 0:
                cells += 1
                box[ny][nx] = 1
                nq.append([ny, nx])
    
    if not q and nq:
        q = nq
        nq = deque()
        day += 1

if cells == m*n:
    print(day)
else:
    print(-1)
