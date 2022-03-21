k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
l, r = 1, max(lan)

while l <= r:
    m = (l + r) // 2

    cnt = 0
    for x in lan:
        cnt += x // m
        if cnt >= n:
            break
    
    if cnt < n:
        r = m - 1
    else:
        l = m + 1

print(r)
