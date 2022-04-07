from math import sqrt
import sys

def sieveOfEratosthenes(x):
    arr = [True] * x
    for i in range(2, int(sqrt(x))+1):
        if arr[i]:
            for j in range(i+i, x, i):
                arr[j] = False
    return arr

input = sys.stdin.readline
n = int(input())
cnt = 0

if n < 2:
    print(cnt)
else:
    arr = sieveOfEratosthenes(n+1)
    primes = []
    for i in range(2, len(arr)):
        if arr[i]:
            primes.append(i)

    l, r = 0, 0
    cur = primes[0]

    while l <= r and l < len(primes):
        if cur == n:
            cnt += 1
            r += 1
            if r == len(primes):
                break
            cur += primes[r]
        elif cur > n:
            cur -= primes[l]
            l += 1
        else:
            r += 1
            if r == len(primes):
                break
            cur += primes[r]
    
    print(cnt)
