from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n):
        clothes, clothes_type = input().split()
        graph[clothes_type].append(clothes)
    mul = 1
    for t in graph.keys():
        mul *= len(graph[t])+1
    print(mul-1)

