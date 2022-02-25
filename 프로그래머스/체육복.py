def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)

    lost2 = lost - reserve
    reserve2 = reserve - lost

    for r in reserve2:
        if r-1 in lost2:
            lost2.remove(r-1)
        elif r+1 in lost2:
            lost2.remove(r+1)

    return n-len(lost2)

n, lost, reserve = 5, [2, 4], [1, 3, 5]
print(solution(n, lost, reserve))