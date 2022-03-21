n = int(input())
k = int(input())

l, r = 1, n**2

while l <= r:
    m = (l + r) // 2

    cnt = 0
    for i in range(1, n+1):
        cnt += min(m//i, n)
    
    if cnt < k:
        l = m + 1
    else:
        r = m - 1

print(l)
