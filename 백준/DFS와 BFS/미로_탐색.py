from collections import deque
row, col = map(int, input().split())
miro = [list(map(int,input())) for _ in range(row)]
q = deque([])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
curlen = 1
q.append([0,0])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= col or ny < 0 or ny >= row:
            continue
        if miro[ny][nx] == 0:
            continue
        if miro[ny][nx] == 1:
            miro[ny][nx] = miro[y][x]+1
            q.append([nx, ny])

print(miro[row-1][col-1])
