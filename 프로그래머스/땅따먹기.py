def solution(land):
    l = len(land)

    for i in range(l-2,-1,-1):
        dp(land, i)

    return max(land[0])

def dp(land, row):
    for i in range(4):
        maxScore = 0
        for j in range(4):
            if i == j:
                continue
            maxScore = max(maxScore, land[row+1][j])
        land[row][i] += maxScore

        


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))
