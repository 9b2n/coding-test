from collections import deque
n = int(input())
town = [list(map(int,input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        if not town[i][j] or visited[i][j]:
            continue
        cur = 0
        q = deque([[i, j]])
        while q:
            y, x = q.popleft()
            visited[y][x] = True
            cur += 1
            for dx, dy in [[0,1], [1,0], [-1, 0], [0, -1]]:
                nx, ny = x+dx, y+dy
                if 0 > nx or nx >= n or 0 > ny or ny >= n:
                    continue
                if not town[ny][nx] or visited[ny][nx]:
                    continue
                if [ny, nx] in q:
                    continue
                q.append([ny, nx])
        result.append(cur)

result.sort()
print(len(result))
for i in result:
    print(i)

