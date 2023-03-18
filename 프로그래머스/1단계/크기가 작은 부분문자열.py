def solution(t, p):
    answer = 0
    maxLen = len(t) - len(p)

    for idx in range(maxLen+1):
        if t[idx:idx+len(p)] <= p:
            answer += 1
    return answer