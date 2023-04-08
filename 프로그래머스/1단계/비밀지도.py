def solution(n, arr1, arr2):
    return [''.join(['#' if c == '1' else ' ' for c in format(arr1[i] | arr2[i], 'b').zfill(n)]) for i in range(n)]


n, arr1, arr2 = 6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))
