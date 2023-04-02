def solution(n):
    a, b = 1, 1

    for i in range(2, n+1):
        b, a = b + a, b

    return b % 1000000007

# 1 - 1
# 2 - 2
# 3 - 3
# 4 - 5
