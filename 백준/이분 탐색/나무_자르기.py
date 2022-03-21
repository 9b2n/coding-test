n, m = map(int, input().split())
trees = list(map(int, input().split()))
l, r = 1, max(trees)

while l <= r:
    mid = (l + r) // 2

    meter = 0

    for tree in trees:
        if mid > tree:
            continue
        meter += tree - mid
        if meter >= m:
            break

    if meter < m:
        r = mid - 1
    else:
        l = mid + 1

print(r)
