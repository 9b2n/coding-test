n = int(input())
rooms = [list(map(int,input().split())) for _ in range(n)]
rooms.sort(key=lambda x: (x[1], x[0]))
cnt = cur = 0
for s, e in rooms:
    if s >= cur:
        cnt += 1
        cur = e
print(cnt)
