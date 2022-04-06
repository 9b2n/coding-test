import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

l, r = 0, len(arr)-1
minSum = abs(arr[l] + arr[r])
result = [arr[l], arr[r]]

while l < r:
    curSum = arr[l] + arr[r]
    absCurSum = abs(curSum)
    if minSum > absCurSum:
        minSum = absCurSum
        result[0], result[1] = arr[l], arr[r]
    if curSum > 0:
        r -= 1
    elif curSum < 0:
        l += 1
    else:
        break

print(*result)
