def solution(s):
    return ' '.join([string.capitalize() for string in s.split(' ')])

s = "     3People         "
print(solution(s))
