p = input()
string = ''
arr, ans = [], []
for s in p:
    if s == '+' or s == '-':
        arr.append(int(string))
        string = ''
        arr.append(s)
    else:
        string = string + s
arr.append(int(string))

flag = True
s = 0
for token in arr:
    if type(token) is int:
        if flag:
            ans.append(token)
        else:
            s += token
    elif token == '-':
        ans.append(-s)
        s = 0
        flag = False
ans.append(-s)
print(sum(ans))
