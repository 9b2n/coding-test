from collections import deque

def solution(order):
    answer = 0

    order = deque(order)
    stack = [i for i in range(1, order[0])]
    origin = deque([i for i in range(order[0], len(order)+1)])

    while order:
        o = order.popleft()
        if stack and stack[-1] == o:
            stack.pop()
            answer += 1
        elif origin and origin[0] == o:
            origin.popleft()
            answer += 1
        else:
            if origin and origin[0] < o:
                stack.append(origin.popleft())
                order.appendleft(o)
            else:
                break

    return answer


# 4 6 5 3 2 1
# [1 2 3]  [4 5 6]