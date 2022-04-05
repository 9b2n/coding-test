from collections import defaultdict
from heapq import heappop, heappush
import sys

INF = float('inf')
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    graph = defaultdict(list)
    dist = [[INF] * (m + 1) for _ in range(n + 1)]

    for _ in range(k):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))
    
    dist[1][0] = 0
    q = []
    heappush(q, (0, 0, 1))
    while q:
        time, cost, u = heappop(q)

        if time > dist[u][cost]:
            continue

        for v, cost2, time2 in graph[u]:
            sumTime = time + time2
            sumCost = cost + cost2
            if sumCost <= m and sumTime < dist[v][sumCost]:
                for i in range(sumCost, m + 1):
                    if sumTime < dist[v][i]:
                        dist[v][i] = sumTime
                    else:
                        break
                heappush(q, (sumTime, sumCost, v))

    print('Poor KCM' if dist[n][m] == INF else dist[n][m])
