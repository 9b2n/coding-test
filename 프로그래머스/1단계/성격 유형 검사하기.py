from collections import defaultdict

def solution(survey, choices):
    answer = []
    score = [i-3 for i in range(7)]
    total = defaultdict(int)
    for personality, choice in zip(survey, choices):
        if score[choice-1] < 0:
            total[personality[0]] += abs(score[choice-1])
        elif score[choice-1] > 0:
            total[personality[1]] += abs(score[choice-1])

    for o, x in ['RT', 'CF', 'JM', 'AN']:
        if total[o] > total[x]:
            answer.append(o)
        elif total[o] < total[x]:
            answer.append(x)
        else:
            answer.append(chr(min(ord(o), ord(x))))

    return ''.join(answer)


survey, choices = ["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]
print(solution(survey, choices))
