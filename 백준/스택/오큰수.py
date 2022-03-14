n = int(input())
nums = list(map(int, input().split()))
nums.reverse()
stack, result = [], []
for num in nums:
    if not stack:
        result.append(-1)
    else:
        while stack and stack[-1] <= num:
            stack.pop()
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
    stack.append(num)

result.reverse()
for x in result:
    print(x, end=' ')
