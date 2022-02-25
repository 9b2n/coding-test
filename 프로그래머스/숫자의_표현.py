def solution(n):
    answer = 0
    for i in range(n, 0, -1):
        answer += find(i, n)
    return answer

def find(i, n):
    for j in range(i, 0, -1):
        n -= j
        if not n:
            return 1
        if n < 0:
            return 0
    return 0

n = 15
print(solution(n))
