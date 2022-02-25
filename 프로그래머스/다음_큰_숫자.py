def solution(n):
    x = bin(n)[2:].count('1')
    while True:
        n += 1
        y = bin(n)[2:]
        if x == y.count('1'):
            return int(y, 2)

n = 15
print(solution(n))
