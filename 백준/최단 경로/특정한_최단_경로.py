from collections import defaultdict
from heapq import heappop, heappush
import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().rstrip().split())

def shortestPath(s):
    q = []
    visited = [float('inf')] * (n+1)
    heappush(q, (0, s))
    visited[s] = 0

    while q:
        w, u = heappop(q)

        if visited[u] < w:
            continue

        for v, w2 in graph[u]:
            if visited[v] > visited[u] + w2:
                visited[v] = visited[u] + w2
                heappush(q, (visited[v], v))
    
    return visited

sPath = shortestPath(1)
v1Path = shortestPath(v1)
v2Path = shortestPath(v2)

result = min(sPath[v1]+v1Path[v2]+v2Path[n], sPath[v2]+v2Path[v1]+v1Path[n])
print(-1) if result == float('inf') else print(result)

