from collections import deque
n, m = map(int, input().split())

arr = deque([i+1 for i in range(n)])
picks = deque(list(map(int, input().split())))

cnt = 0
while picks:
    curPick = picks.popleft()
    if arr[0] == curPick:
        arr.popleft()
    else:
        idx = arr.index(curPick)
        if idx <= len(arr) - idx:
            for _ in range(idx):
                arr.append(arr.popleft())
                cnt += 1
        else:
            for _ in range(len(arr) - idx):
                arr.appendleft(arr.pop())
                cnt += 1
        arr.popleft()
print(cnt)
