def solution(numbers):
    answer = []
    stack = []

    while numbers:
        cur = numbers.pop()

        flag = True
        while stack and flag:
            big = stack[-1]
            if big > cur:
                answer.append(big)
                flag = False
            else:
                stack.pop()

        stack.append(cur)

        if flag:
            answer.append(-1)

    answer.reverse()

    return answer


numbers = [2, 3, 3, 5]
print(solution(numbers))
