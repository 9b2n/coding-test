m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
dp = [[-1]*n for _ in range(m)]

def dfs(curY, curX):
    if curY == m-1 and curX == n-1:
        return 1
    if dp[curY][curX] != -1:
        return dp[curY][curX]
    dp[curY][curX] = 0
    for y, x in zip(dy, dx):
        ny, nx = curY+y, curX+x
        if 0 <= ny < m and 0 <= nx < n:
            if arr[ny][nx] < arr[curY][curX]:
                dp[curY][curX] += dfs(ny, nx)
    return dp[curY][curX]

print(dfs(0, 0))
