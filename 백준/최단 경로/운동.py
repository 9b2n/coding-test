from collections import defaultdict
from heapq import heappop, heappush
import sys

# 다익스트라
def shortestPath(s):
    dist = [float('inf')] * (n+1)
    q = []
    heappush(q, (0, s))

    while q:
        w, u = heappop(q)

        if dist[u] < w:
            continue

        for v, w2 in graph[u]:
            cost = w + w2
            if cost < dist[v]:
                dist[v] = cost
                heappush(q, (cost, v))
    
    return dist

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]

# 다익스트라 풀이
# graph = defaultdict(list)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
    
# result = min([shortestPath(i)[i] for i in range(1, n+1)])

# 플로이드워셜 풀이
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = min([graph[i][i] for i in range(1, n+1)])

print(-1 if result == float('inf') else result)
