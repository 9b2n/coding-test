def solution(babbling):
    answer = 0
    only = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        strings = only
        for string in strings:
            if string*2 in word:
                break
            word = word.replace(string, " ")

        if not word.strip():
            answer += 1
    return answer


