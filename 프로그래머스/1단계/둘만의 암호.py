def solution(s, skip, index):
    answer = []
    skip = set(skip)
    arr = [chr(ord('a') + i) in skip for i in range(26)]

    for alpha in s:
        diff = index
        original = ord(alpha) - ord('a') + 1
        while diff:
            if not arr[original % 26]:
                diff -= 1

            original += 1

        answer.append(chr(ord('a') + (original - 1) % 26))

    return "".join(answer)


s, skip, index = "aukks", "wbqd", 5
print(solution(s, skip, index))
