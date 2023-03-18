def solution(s):
    answer = 1
    origin = s[0]
    same = diff = 0

    for idx, ch in enumerate(s[:-1]):
        if origin == ch:
            same += 1
        else:
            diff += 1

        if same == diff:
            answer += 1
            origin = s[idx+1]
            same = diff = 0
    return answer


s = "abracadabra"
print(solution(s))
