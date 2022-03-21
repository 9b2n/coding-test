n, c = map(int, input().split())
houses = sorted([int(input()) for _ in range(n)])

l, r = 1, houses[-1] - houses[0]

while l <= r:
    m = (l + r) // 2

    cur = houses[0]
    cnt = 1

    for i in range(1, len(houses)):
        if houses[i] >= cur + m:
            cnt += 1
            cur = houses[i]
            if cnt >= c:
                break
        
    if cnt < c:
        r = m - 1
    else:
        l = m + 1

print(r)
