def solution(sequence, k):
    answer = []
    l, r = 0, -1
    s = 0

    while l < len(sequence):
        if s < k:  # 합이 k보다 작을 때
            r += 1
            if r >= len(sequence):
                break
            s += sequence[r]
        else:
            s -= sequence[l]
            l += 1
        if s == k:
            answer.append([l, r])

    return sorted(answer, key=lambda x: (x[1] - x[0], x[0]))[0]


sequence, k = [1, 2, 3, 4, 5], 7
print(solution(sequence, k))

# l 0  0 0 0 0  1 1 2 2 3 3 4 4
# r -1 0 1 2 3  3 3 3 3 3 4 4 5
# s 0  1 3 6 10 9 7 7 4 4 9 5 5
# k 7
# [0, 3] [1, 3] [2, 3] [3 4]
