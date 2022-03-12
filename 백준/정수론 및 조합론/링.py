n = int(input())
rings = list(map(int, input().split()))
first = rings[0]

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

for i in range(1, n):
    GCD = gcd(first, rings[i])
    print(str(first//GCD)+"/"+str(rings[i]//GCD))
