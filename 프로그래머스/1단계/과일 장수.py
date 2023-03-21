def solution(k, m, score):
    answer = 0
    score.sort()
    print(score)
    minV = k
    num = 0
    while score:
        minV = min(minV, score.pop())
        num += 1
        if num % m == 0:
            num = 0
            answer += minV * m
    return answer


k, m, score = 3, 4, [1, 2, 3, 1, 2, 3, 1]
print(solution(k, m, score))
