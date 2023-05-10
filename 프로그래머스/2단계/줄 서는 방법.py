from math import factorial

def solution(n, k):
    l = [i + 1 for i in range(n)]
    return line(n, k, l)

def line(n, k, l):
    if n == 1:
        return l

    x = factorial(n - 1)
    q = (k-1)//x
    k = k % x
    return [l.pop(q)] + line(n - 1, k, l)


print(solution(3, 1))
