from collections import defaultdict
from heapq import heappop, heappush
import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
sv = int(input().rstrip())
graph = defaultdict(list)
q = []
dis = [float('inf')] * (n+1)

for _ in range(m):
    s, e, w = map(int, input().rstrip().split())
    graph[s].append((e, w))

dis[sv] = 0
heappush(q, (0, sv))
while q:
    w, u = heappop(q)

    if dis[u] < w:
        continue

    for v, w2 in graph[u]:
        if w + w2 < dis[v]:
            dis[v] = w + w2
            heappush(q, (dis[v], v))

for i in range(1, n+1):
    print('INF') if dis[i] == float('inf') else print(dis[i]) 
