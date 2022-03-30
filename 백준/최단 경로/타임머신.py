import sys

def bellmanFold(s):
    dist[s] = 0
    # n번 반복
    for i in range(n):
        # 모든 간선 확인
        for j in range(m):
            u, v, w = edges[j]
            # 현재 간선을 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                # n번째에서도 값이 갱신되면 음수 사이클 존재
                if i == n - 1:
                    return True
    return False


input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
edges = []
dist = [float('inf')] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    edges.append((a, b, c))

isNegativeCycle = bellmanFold(1)

if isNegativeCycle:
    print(-1)
else:
    for i in range(2, n + 1):
        print(-1 if dist[i] == float('inf') else dist[i])
