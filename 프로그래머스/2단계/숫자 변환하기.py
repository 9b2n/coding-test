from collections import deque


def solution(x, y, n):
    dis = [0] * (y + 1)
    cal = [lambda a: a + n, lambda a: a * 2, lambda a: a * 3]
    q = deque()
    q.append(x)

    if x == y:
        return 0

    while q:
        nx = q.popleft()
        for f in cal:
            cur = f(nx)
            if cur > y or dis[cur]:
                continue
            if cur == y:
                return dis[nx] + 1
            q.append(cur)
            dis[cur] = dis[nx] + 1

    return -1


x, y, n = 10, 40, 5
print(solution(x, y, n))
