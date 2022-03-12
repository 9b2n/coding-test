from math import sqrt

n = int(input())
arr = sorted([int(input()) for _ in range(n)])
diff = [arr[i] - arr[i-1] for i in range(n)]

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

curGCD = diff[0]
for d in diff:
    curGCD = gcd(curGCD, d)

result = []
for i in range(2, int(sqrt(curGCD))+1):
    if curGCD % i == 0:
        result.append(i)
        result.append(curGCD//i)
result.append(curGCD)

result = sorted(list(set(result)))
for i in result:
    print(i, end=' ')
