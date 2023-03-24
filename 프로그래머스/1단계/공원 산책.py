def solution(park, routes):
    mapping = {
        'N': [-1, 0],
        'S': [1, 0],
        'W': [0, -1],
        'E': [0, 1]
    }
    y, x = findStartPoint(park)
    row, col = len(park)-1, len(park[0])-1

    for route in routes:
        dr, dis = route.split()
        dis = int(dis)

        dy, dx = mapping[dr][0] * int(dis), mapping[dr][1] * int(dis)

        if y + dy < 0 or y + dy > row or x + dx < 0 or x + dx > col:
            continue

        flag = False
        for d in range(1, dis + 1):
            if park[y + mapping[dr][0] * d][x + mapping[dr][1] * d] == 'X':
                flag = True
                break

        if flag:
            continue

        y, x = y + dy, x + dx

    return [y, x]


def findStartPoint(park):
    for i, line in enumerate(park):
        for j, point in enumerate(line):
            if point == 'S':
                return i, j


park, routes = ["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]
print(solution(park, routes))
