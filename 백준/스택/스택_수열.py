n = int(input())
arr, opArr, nums = [], [], []

for i in range(n):
    nums.append(int(input()))

x = 1
flag = True
for num in nums:
    if not arr or arr[-1] != num:
        for i in range(x, num+1):
            arr.append(i)
            opArr.append('+')
            x += 1
        if arr[-1] != num:
            flag = False
            break
        else:
            arr.pop()
            opArr.append('-')
    else:
        arr.pop()
        opArr.append('-')

if flag:
    for op in opArr:
        print(op)
else:
    print('NO')
