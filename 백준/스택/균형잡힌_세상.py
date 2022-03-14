while True:
    string = input()
    stack = []
    if string == '.':
        break
    for s in string:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] != '(':
                stack.append(s)
                break
            else:
                stack.pop()
        elif s == '[':
            stack.append(s)
        elif s == ']':
            if not stack or stack[-1] != '[':
                stack.append(s)
                break
            else:
                stack.pop()
    print('no') if stack else print('yes')
