from math import factorial
t = int(input())
arr = [list(map(int, input().split())) for _ in range(t)]

for n, m in arr:
    x, y = max(n, m), min(n, m)
    print(factorial(x)//(factorial(x-y)*factorial(y)))
