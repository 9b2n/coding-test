import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    files = list(map(int, sys.stdin.readline().strip().split()))
    dp = [[0]*n for _ in range(n)]

    for i in range(n-1):
        dp[i][i+1] = files[i] + files[i+1]
        for j in range(i+2, n):
            dp[i][j] = dp[i][j-1] + files[j]
    
    for x in range(2, n):
        for i in range(n-x):
            j = i + x
            dp[i][j] += min([dp[i][k]+dp[k+1][j] for k in range(i, j)])
    print(dp[0][n-1])
