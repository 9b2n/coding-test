from collections import deque
import sys

n = int(input())
q = deque()

for _ in range(n):
    ops = sys.stdin.readline().split()
    if ops[0] == 'push_front':
        q.appendleft(ops[1])
    elif ops[0] == 'push_back':
        q.append(ops[1])
    elif ops[0] == 'pop_front':
        print(q.popleft()) if q else print(-1)
    elif ops[0] == 'pop_back':
        print(q.pop()) if q else print(-1)
    elif ops[0] == 'size':
        print(len(q))
    elif ops[0] == 'empty':
        print(0) if q else print(1)
    elif ops[0] == 'front':
        print(q[0]) if q else print(-1)
    else:
        print(q[-1]) if q else print(-1)
