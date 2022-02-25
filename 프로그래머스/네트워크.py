# def solution(n, computers):
#     answer = 0
#     net = set()
#     for i in range(n):
#         re, net = dfs(net, i, computers)
#         answer += re
        
#     return answer

# def dfs(net, i, computers):
#     if i in net:
#         return 0, net
#     net.add(i)
#     neighbors = computers[i]
#     for ni in range(len(neighbors)):
#         if ni != i and neighbors[ni]:
#             if ni not in net:
#                 dfs(net, ni, computers)
#     return 1, net
    
def solution(n, computers):
    nws = []
    for i in range(n):
        dfs(computers, n, i, nws)
    return len(nws)

def dfs(computers, n, i, nws):
    flag = True
    for nw in nws:
        if i in nw:
            net = nw
            flag = False
            break
    if flag:
        net = {i}
        nws.append(net)

    for j in range(n):
        if j != i and computers[i][j]:
            if j not in net:
                net.add(j)
                dfs(computers, n, j, nws)

n, computers = 3,		[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))