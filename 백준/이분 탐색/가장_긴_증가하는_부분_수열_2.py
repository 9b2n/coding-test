n = int(input())
arr = list(map(int, input().split()))
dp = [0]

for i in range(n):
    l, r = 0, len(dp) - 1

    while l <= r:
        m = (l + r) // 2
        if dp[m] < arr[i]:
            l = m + 1
        else:
            r = m - 1
        
    if l >= len(dp):
        dp.append(arr[i])
    else:
        dp[l] = arr[i]

print(len(dp) - 1)
