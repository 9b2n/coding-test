n = int(input())
arr = list(map(int,input().split()))
maxV = cur = 0

for x in arr:
    cur += x
    if cur > maxV:
        maxV = cur
    elif cur < 0:
        cur = 0

print(maxV) if maxV else print(max(arr))

