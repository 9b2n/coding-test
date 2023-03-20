def solution(n, m, section):
    answer = 0
    cur = section[0]

    for s in section:
        if s < cur:
            continue
        answer += 1
        cur = s+m

    return answer
