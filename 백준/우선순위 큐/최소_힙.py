from heapq import heappop, heappush
import sys

n = int(sys.stdin.readline().strip())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x:
        heappush(heap, x)
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0)
