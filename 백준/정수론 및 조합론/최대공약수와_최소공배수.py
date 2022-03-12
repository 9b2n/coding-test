n, m = map(int, input().split())
a, b = max(n, m), min(n, m)

def gcd(n, m):
    while m > 0:
        tmp = n%m
        n = m
        m = tmp
    return n

GCD = gcd(a, b)
print(GCD)
print(GCD * (n//GCD) * (m//GCD))
