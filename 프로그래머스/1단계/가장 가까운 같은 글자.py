def solution(s):
    answer = []
    arr = {}

    for idx, c in enumerate(s):
        answer.append(idx - arr[c] if c in arr else -1)
        arr[c] = idx
    return answer

s = "banana"
print(solution(s))