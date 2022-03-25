import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())
MAX = 10**5
point = [0] * (MAX + 1)

q = deque([n])

while q:
    x = q.popleft()
    if x == k:
        print(point[x])
        break
    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= MAX and not point[nx]:
            q.append(nx)
            point[nx] = point[x] + 1
