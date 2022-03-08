string1 = input()
string2 = input()
n1 = len(string1)
n2 = len(string2)
dp = [[0] * (n2+1) for _ in range(n1+1)]

for i in range(n1):
    for j in range(n2):
        if string1[i] == string2[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[n1][n2])
