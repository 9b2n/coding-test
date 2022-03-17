n, k , m = map(int, input().split())

def divideNConquer(n, k, m):
    if k == 1:
        return n%m

    dnc = divideNConquer(n, k//2, m)
    if k % 2:
        return (dnc*dnc*n)%m
    else:
        return (dnc*dnc)%m

print(divideNConquer(n, k, m))
