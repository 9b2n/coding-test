from collections import defaultdict


def solution(k, tangerine):
    answer = 0
    d = defaultdict(int)

    for t in tangerine:
        d[t] += 1

    for n in sorted(d.values(), reverse=True):
        if k <= 0:
            break
        answer += 1
        k -= n

    return answer


k, tangerine = 6, [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))
