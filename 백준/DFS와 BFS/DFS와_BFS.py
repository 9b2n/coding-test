from collections import defaultdict, deque
n, m, v = map(int, input().split())
graph = defaultdict(list)

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for key in graph.keys():
    graph[key].sort()

def dfs(graph, n):
    print(n, end=" ")
    check[n] = True
    for x in graph[n]:
        if check[x]:
            continue
        dfs(graph, x)

def bfs(graph, n):
    queue = deque([n])
    while queue:
        x = queue.popleft()
        check[x] = True
        print(x, end=" ")
        for i in graph[x]:
            if not check[i] and i not in queue:
                queue.append(i)

check = [False] * (n + 1)
dfs(graph, v)
print()
check = [False] * (n + 1)
bfs(graph, v)





