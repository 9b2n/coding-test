def solution(elements):
    s = set()
    n = len(elements)
    for l in range(1, n):
        for i in range(n):
            if i+l > n:
                s.add(sum(elements[i:n]) + sum(elements[:i+l-n]))
            else:
                s.add(sum(elements[i:i+l]))

    s.add(sum(elements))
    return len(s)
