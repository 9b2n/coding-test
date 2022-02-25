def solution(skill, skill_trees):
    answer = 0

    for st in skill_trees:
        sIdx = 0
        flag = True
        
        for s in st:
            if s in skill:
                if skill.index(s) == sIdx:
                    sIdx += 1
                else:
                    flag = False
                    break
        if flag:
            answer += 1

    return answer

skill, skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
