from bisect import bisect_left
from collections import defaultdict
from itertools import combinations


def solution(infos, queries):
    answer = []
    people = defaultdict(list)
    for info in infos:
        info = info.split()
        score = int(info[-1])
        other = info[:-1]
        for i in range(5):
            cases = list(combinations([0, 1, 2, 3], i))
            for case in cases:
                tmp = other.copy()
                for idx in case:
                    tmp[idx] = '-'
                key = ''.join(tmp)
                people[key].append(score)

    for v in people.values():
        v.sort()

    for query in queries:
        query = query.split(' and ')
        food, score = query.pop().split()
        query.append(food)
        qKey = ''.join(query)
        qScore = int(score)
        cnt = 0
        if qKey in people:
            scoreList = people[qKey]
            idx = bisect_left(scoreList, qScore)
            cnt = len(scoreList) - idx
        answer.append(cnt)
    return answer

info, query = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution(info, query))
