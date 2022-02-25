def solution(routes):
    answer = 0
    routes.sort(key= lambda x : x[1])
    minE = routes[0][1]

    for r in routes:
        if r[0] > minE:
            answer += 1
            minE = r[1]

    return answer + 1

routes = 	[[-20, 15]]
print(solution(routes))