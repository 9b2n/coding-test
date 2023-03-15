from collections import defaultdict


def solution(keymap, targets):
    answer = []
    keyDict = defaultdict(int)
    for row in keymap:
        for idx in range(len(row)):
            if keyDict[row[idx]] == 0:
                keyDict[row[idx]] = idx+1
            else:
                keyDict[row[idx]] = min(keyDict[row[idx]], idx + 1)

    print(keyDict)

    for string in targets:
        s = 0
        for char in string:
            if keyDict[char] == 0:
                s = -1
                break
            else:
                s += keyDict[char]
        answer.append(s)
    return answer


keymap, targets = ["ABACD", "BCEFD"], ["ABCD", "AABB"]
print(solution(keymap, targets))
