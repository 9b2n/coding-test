n = int(input())
for _ in range(n):
    string = input()
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(s)
                break
    print('NO') if stack else print('YES')
