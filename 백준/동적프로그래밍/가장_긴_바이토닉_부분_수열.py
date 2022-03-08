n = int(input())
arr = list(map(int, input().split()))
upDP, downDP = [1] * n, [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            upDP[i] = max(upDP[i], upDP[j]+1)

arr.reverse()
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            downDP[i] = max(downDP[i], downDP[j]+1)

dp = [upDP[i] + downDP[n-i-1] -1 for i in range(n)]

print(max(dp))
