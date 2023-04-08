def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        a = arr1[i] | arr2[i]
        answer.append(''.join(['#' if c == '1' else ' ' for c in format(a, 'b').zfill(n)]))

    return answer


n, arr1, arr2 = 6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))
