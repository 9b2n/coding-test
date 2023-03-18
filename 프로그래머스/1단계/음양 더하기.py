def solution(absolutes, signs):
    return sum([n if op else -n for n, op in zip(absolutes, signs)])
