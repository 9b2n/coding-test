from collections import deque
from math import sqrt

def solution(n, k):
    answer = 0
    string = nTokNumber(n, k)
    temp = ''

    for s in string:
        if s == '0':
            if temp != '' and isPrime(int(temp)):
                answer += 1
            temp = ''
            continue
        temp = temp + s
    if temp != '' and isPrime(int(temp)):
        answer += 1
    return answer

def nTokNumber(n, k):
    string = deque([])
    while n >= k:
        x = n % k
        n = n // k
        string.appendleft(x)
    string.appendleft(n)
    return ''.join(str(_) for _ in string)

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, sqrt(n)+1):
        if n % i == 0:
            return False
    return True

n, k = 	13, 10
print(solution(n, k))
