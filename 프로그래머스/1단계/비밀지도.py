def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        a = arr1[i] | arr2[i]
        b = format(a, 'b')

        new = []
        if len(b) < n:
            new.append(' ' * (n-len(b)))
        for c in b:
            new.append('#' if c == '1' else ' ')

        answer.append(''.join(new))

    return answer


n, arr1, arr2 = 6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))
