def solution(word):
    answer = 0
    alpha = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}

    for i in range(len(word)):
        gap = 0
        for j in range(5-i):
            gap = gap * 5 + 1
        answer += (alpha[word[i]] * gap + 1)

    return answer

word = 	"EIO"
print(solution(word))
