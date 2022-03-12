n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
result = []

def gcd(x, y):
    while y > 0:
        tmp = x%y
        x = y
        y = tmp
    return x

for x, y in arr:
    a, b = max(x, y), min(x, y)
    GCD = gcd(a, b)
    print(a*b//GCD)
