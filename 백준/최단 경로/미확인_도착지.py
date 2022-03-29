from collections import defaultdict
from heapq import heappop, heappush
import sys

def shortestPath(s):
        q = []
        dist = [float('inf')] * (n + 1)
        heappush(q, (0, s))
        dist[s] = 0

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
T = int(input().rstrip())

for _ in range(T):
    graph = defaultdict(list)
    n, m, t = map(int, input().rstrip().split())
    s, g, h = map(int, input().rstrip().split())
    x = 0

    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        if (a == g and b == h) or (a == h and b == g):
            x = c
    
    sPath = shortestPath(s)
    hPath = shortestPath(h)
    gPath = shortestPath(g)
    result = []
    for _ in range(t):
        d = int(input().rstrip())
        path1 = sPath[h] + x + gPath[d]
        path2 = sPath[g] + x + hPath[d]
        path = min(path1, path2)
        if path != float('inf') and path == sPath[d]:
            result.append(d)
    print(*sorted(result))


