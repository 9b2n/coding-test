# 미완
def solution(arrows):
    answer = 0
    dot = [(0,0)]
    move = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    cur = (0,0)
    for num in arrows:
        cur = (cur[0] + move[num][0], cur[1] + move[num][1])
        if cur in dot:
            answer += 1
        else:
            dot.append(cur)
    return answer

arrows = [6,4,2,0]
print(solution(arrows))