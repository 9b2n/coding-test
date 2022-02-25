def solution(m, n, puddles):
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                arr[i][j] = 1
            elif [j+1,i+1] in puddles:
                continue
            else:
                arr[i][j] = (arr[i][j-1] + arr[i-1][j]) % 1000000007

    return arr[n-1][m-1]

# def solution(m, n, puddles):
#     arr = [[1] * m for _ in range(n)]
#     for p in puddles:
#         arr[p[1]-1][p[0]-1] = 0
    
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 0 or (i == 0 and j == 0):
#                 continue
#             elif i == 0:
#                 arr[i][j] = arr[i][j-1] % 1000000007
#             elif j == 0:
#                 arr[i][j] = arr[i-1][j] % 1000000007
#             else:
#                 arr[i][j] = (arr[i][j-1] + arr[i-1][j]) % 1000000007
#     return arr[n-1][m-1]

m,n,puddles = 4, 3, [[2,2]]
print(solution(m,n,puddles))