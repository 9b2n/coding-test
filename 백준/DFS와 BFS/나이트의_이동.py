from collections import deque
import sys

input = sys.stdin.readline
t = int(input().rstrip())
move = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]

for _ in range(t):
    n = int(input().rstrip())
    visited = [[0] * n for _ in range(n)]
    y, x = map(int, input().rstrip().split())
    dy, dx = map(int, input().rstrip().split())

    q = deque()
    q.append([y, x])

    while q:
        y, x = q.popleft()
        if y == dy and x == dx:
            print(visited[y][x])
            break

        for i, j in move:
            ny = y + i
            nx = x + j
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])

