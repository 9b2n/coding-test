def solution(ingredient):
    answer = 0
    stack = []

    for x in ingredient:
        stack.append(x)
        if x == 1:
            if len(stack) > 3:
                if stack[-4:] == [1, 2, 3, 1]:
                    for i in range(4):
                        stack.pop()
                    answer += 1
    return answer


ingredient = 	[2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))
