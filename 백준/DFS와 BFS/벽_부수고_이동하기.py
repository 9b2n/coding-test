from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append([0, 0, 0])

flag = False
while q:
    y, x, z = q.popleft()

    if y == n-1 and x == m-1:
        flag = True
        print(visited[y][x][z]+1)
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] == 0 and visited[ny][nx][z] == 0:
                visited[ny][nx][z] = visited[y][x][z] + 1
                q.append([ny, nx, z])
            elif arr[ny][nx] == 1 and z == 0:
                visited[ny][nx][z+1] = visited[y][x][z] + 1
                q.append([ny, nx, z+1])

if not flag:
    print(-1)
