from math import factorial
n = int(input())
string = list(str(factorial(n)))
string.reverse()
cnt = 0
for i in string:
    if i != '0':
        break
    cnt += 1
print(cnt)
