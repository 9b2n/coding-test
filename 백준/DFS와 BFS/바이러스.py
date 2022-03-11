from collections import defaultdict

graph = defaultdict(list)
n = int(input())
e = int(input())

visited = [False] * (n+1)

for _ in range(e):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(graph, v):
    global visited

    visited[v] = True

    for x in graph[v]:
        if not visited[x]:
            dfs(graph, x)

dfs(graph, 1)

print(sum(visited)-1)
