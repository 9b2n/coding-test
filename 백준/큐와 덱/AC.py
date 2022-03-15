from collections import deque
import sys
t = int(sys.stdin.readline().strip())

for _ in range(t):
    functions = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    nums = deque(sys.stdin.readline().strip()[1:-1].split(','))
    direction = True
    flag = True
    for f in functions:
        if f == 'R':
            direction = not direction
        else:
            if not n:
                print('error')
                flag = False
                break
            else:
                if direction:
                    nums.popleft()
                else:
                    nums.pop()
                n -= 1
    
    if not direction:
        nums.reverse()
    if flag:
        print('['+','.join(nums)+']')
    