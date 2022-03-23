from heapq import heappop, heappush
import sys

n = int(sys.stdin.readline().strip())
front = []
end = []


for _ in range(n):
    x = int(sys.stdin.readline().strip())

    if len(front) == len(end):
        heappush(front, (-x, x))
    else:
        heappush(end, x)
    
    if end and front[0][1] > end[0]:
        minV, maxV = heappop(end), heappop(front)[1]
        heappush(front, (-minV, minV))
        heappush(end, maxV)
    
    print(front[0][1])
