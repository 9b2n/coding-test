from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)

    while True:
        if answer > len(queue1) * 3:
            return -1
        if s1 > s2:
            new = q1.popleft()
            s1 -= new
            s2 += new
            q2.append(new)
        elif s1 < s2:
            new = q2.popleft()
            s2 -= new
            s1 += new
            q1.append(new)
        else:
            return answer

        answer += 1


queue1, queue2 = [1, 2, 1, 2], [1, 10, 1, 2]
print(solution(queue1, queue2))
