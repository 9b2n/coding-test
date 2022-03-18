n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for diff in range(1, n):
    for s in range(n-diff):
        e = s + diff
        dp[s][e] = 2**31
        for m in range(s, e):
            dp[s][e] = min(dp[s][e], dp[s][m] + dp[m+1][e] + matrix[s][0]*matrix[m][1]*matrix[e][1] )
print(dp[0][n-1])
