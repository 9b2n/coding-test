def solution(s):
    nList = list(map(int, s.split()))
    return str(min(nList)) + ' ' + str(max(nList))

s = "-1 -2 -3 -4"
print(solution(s))
