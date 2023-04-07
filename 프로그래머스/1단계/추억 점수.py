def solution(name, yearning, photo):

    m = {n: y for n, y in zip(name, yearning)}
    return [sum([m[person] if person in m else 0 for person in p]) for p in photo]
