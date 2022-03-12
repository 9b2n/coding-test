from math import factorial
# 이항계수 (n k)는  nCk
n, k = map(int, input().split())

print(factorial(n)//(factorial(n-k)*factorial(k)))
