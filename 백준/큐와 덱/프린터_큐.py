from collections import deque
import heapq

n = int(input())
for _ in range(n):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    cnt = 0
    q, h = deque(), []
    for i in range(n):
        q.append((i, -priorities[i]))
        heapq.heappush(h, -priorities[i])
    while q:
        idx, p = q.popleft()
        if p == h[0]:
            heapq.heappop(h)
            cnt += 1
            if idx == m:
                print(cnt)
                break
        else:
            q.append((idx, p))
