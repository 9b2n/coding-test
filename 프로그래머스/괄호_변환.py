def solution(p):
    answer = ''
    reverseBracket = { '(' : ')', ')': '('}
    if not p:
        return p
    u, v, isRight = minCoupleOfBrackets(p)
    if isRight:
        return u + solution(v)
    else:
        answer += '(' + solution(v) + ')'
        for i in range(1, len(u)-1):
            answer += reverseBracket[u[i]]
        return answer

def minCoupleOfBrackets(s):
    stack = []
    coupleCnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            coupleCnt += 1
        else:
            if stack:
                stack.pop()
            coupleCnt -= 1
        if not coupleCnt:
            break
    isRight = False if stack else True
    return (s[:i+1], s[i+1:], isRight)

p = "()))((()"
print(solution(p))
