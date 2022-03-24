import sys


n, k = map(int, sys.stdin.readline().strip().split())

def dfs(n, k, cnt):
    print(n, k, cnt)
    if n > k:
        return float('inf')
    if n == k:
        return cnt
    cnt += 1
    if k%2:
        return dfs(n, k-1, cnt)
    else:
        return min(dfs(n, k//2, cnt), dfs(n, k-1, cnt))

sec = dfs(n, k, 0)
print(sec)
