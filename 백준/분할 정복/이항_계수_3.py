n, k = map(int, input().split())
m = 1000000007

def power(n, e):
    global m

    if e == 1:
        return n % m
    ie = power(n, e//2)

    if e % 2:
        return ie * ie * n % m
    return ie * ie % m

fact = [1 for _ in range(n+1)]

for i in range(2, n+1):
    fact[i] = fact[i-1] * i % m

x = fact[n]
y = fact[k] * fact[n-k] % m
ie = power(y, m-2)

print(x * ie % m)
