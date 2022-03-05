n = int(input())
arr = [int(input()) for _ in range(n)]

if n < 3:
    print(sum(arr))
else:
    dp = []
    dp.append(arr[0])
    dp.append(arr[0]+arr[1])
    dp.append(max(dp[1], arr[0]+arr[2], arr[1]+arr[2]))
    for i in range(3, n):
        dp.append(max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i], dp[i-1]))
    print(dp.pop())
