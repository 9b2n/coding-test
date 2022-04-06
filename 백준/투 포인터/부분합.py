import sys

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

MAX = 100001
l, r = 0, 0
curSum = arr[0]
minLen = 1 if curSum >= s else MAX

while l < len(arr):
    if curSum < s:
        r += 1
        if r == len(arr):
            break
        curSum += arr[r]
    else:
        minLen = min(minLen, r-l+1)
        curSum -= arr[l]
        l += 1

print(minLen if minLen != MAX else 0)
