from collections import Counter, defaultdict

def solution(topping):
    answer = 0

    before = defaultdict(int)
    after = Counter(topping)

    sb = set(before)
    sa = set(after)

    for t in topping:
        before[t] += 1
        after[t] -= 1

        if before[t] == 1:
            sb.add(t)

        if after[t] == 0:
            sa.remove(t)

        if len(sb) == len(sa):
            answer += 1

    return answer
