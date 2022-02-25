from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for per in permutations(dungeons):
        cur = k
        cnt = 0
        for x, y in per:
            if cur >= x:
                cur -= y
                cnt += 1
        answer = max(answer, cnt)

    return answer

k, dungeons = 80, [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))
