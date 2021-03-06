n = int(input())

dp = [[0] + [1] * 9]

for i in range(1, n):
    arr = []
    for j in range(10):
        if j == 0:
            arr.append(dp[i-1][1])
        elif j == 9:
            arr.append(dp[i-1][8])
        else:
            arr.append(dp[i-1][j-1]+dp[i-1][j+1])
    dp.append(arr)

print(sum(dp[n-1]) % 1000000000)
