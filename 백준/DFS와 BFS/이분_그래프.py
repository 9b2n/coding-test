from collections import defaultdict, deque
import sys

input = sys.stdin.readline
k = int(input().rstrip())

for _ in range(k):
    n, m = map(int, input().rstrip().split())
    graph = defaultdict(list)
    colors = [-1] * (n+1)

    for _ in range(m):
        s, e = map(int, input().rstrip().split())
        graph[s].append(e)
        graph[e].append(s)
    
    q = deque()
    color = True
    flag = True
    for i in range(1, n+1):
        if colors[i] == -1:
            q.append(i)
            colors[i] = color
            while q:
                v = q.popleft()
                for w in graph[v]:
                    if colors[w] == -1:
                        q.append(w)
                        colors[w] = not colors[v]
                    else:
                        if colors[w] == colors[v]:
                            flag = False
    print('YES') if flag else print('NO')





