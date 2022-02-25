n = int(input())
arr = [list(map(int,input().split()))[:n] for _ in range(n)]
teamA = []
teamAll = {i for i in range(n)}
cur_idx = 0
minV = 1000

def exp(team): # 팀 점수 계산
    s = 0
    for i in team:
        for j in team:
            s += arr[i][j]
    return s

def dfs(depth, cur_idx): # 팀 조합 짜기
    global n
    global minV

    if depth == n//2-1: # n//2 인원까지 구했다면 stop
        teamB = teamAll - set(teamA)
        expA = exp(teamA)
        expB = exp(teamB)
        minV = min(minV, abs(expA-expB))
        return
    
    for i in range(cur_idx+1, n):
        teamA.append(i)
        dfs(depth+1, i)
        teamA.pop()

teamA.append(cur_idx)
dfs(0, cur_idx)
print(minV)