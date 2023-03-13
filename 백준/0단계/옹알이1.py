from itertools import combinations


def solution(babbling):
    answer = 0
    for word in babbling:
        possible = ["aya", "ye", "woo", "ma"]
        while possible:
            start = len(possible)
            for p in possible:
                if word.startswith(p):
                    possible.pop(possible.index(p))
                    if len(word) == len(p):
                        word = ''
                    else:
                        word = word[len(p):]

            if start == len(possible):
                break

            if len(word) == 0:
                answer += 1
                break

    return answer


babbling = ["aya", "yee", "u", "maa", "wyeoo"]
print(solution(babbling))
