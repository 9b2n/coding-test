from collections import deque

n, k = map(int, input().split())
q = deque([i+1 for i in range(n)])
result = []

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(str(q.popleft()))

print('<'+', '.join(result)+'>')
