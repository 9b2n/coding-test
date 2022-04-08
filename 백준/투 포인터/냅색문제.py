from itertools import combinations
import sys

input = sys.stdin.readline
n, c = map(int, input().split())
arr = list(map(int, input().split()))
arrA, arrB = arr[:n//2], arr[n//2:]
sumA, sumB = [], []

for i in range(len(arrA)+1):
    for combi in combinations(arrA, i):
        sumA.append(sum(combi))

for i in range(len(arrB)+1):
    for combi in combinations(arrB, i):
        sumB.append(sum(combi))

sumB.sort()
cnt = 0
for i in sumA:

    if i > c:
        continue

    s, e = 0, len(sumB)-1
    while s <= e:
        m = (s + e) // 2

        if sumB[m] <= c - i:
            s = m + 1
        else:
            e = m - 1
    
    cnt += s

print(cnt)
