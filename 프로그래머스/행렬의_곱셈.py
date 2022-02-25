def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            e = 0
            for k in range(len(arr1[0])):
                e += arr1[i][k] * arr2[k][j]
            row.append(e)
        answer.append(row)
    return answer

arr1, arr2 = [[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]
print(solution(arr1, arr2))
