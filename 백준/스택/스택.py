import sys
n = int(input())
stack = []
for _ in range(n):
    ops = sys.stdin.readline().split()
    if ops[0] == 'push': stack.append(ops[1]),
    elif ops[0] == 'pop': print(stack.pop()) if stack else print(-1),
    elif ops[0] == 'top': print(stack[-1]) if stack else print(-1),
    elif ops[0] == 'size': print(len(stack)),
    else: print(0) if stack else print(1),
