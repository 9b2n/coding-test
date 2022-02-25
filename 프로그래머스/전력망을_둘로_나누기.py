from collections import defaultdict

def solution(n, wires):
    answer = [-1]
    graph = defaultdict(list)

    for n1, n2 in wires:
        graph[n1].append(n2)
        graph[n2].append(n1)

    def dfs(node_num, parent_node_num):
        child_num = 0
        for child_node_num in graph[node_num]:
            if child_node_num != parent_node_num:
                child_num += dfs(child_node_num, node_num)
        
        if abs(n//2 - (child_num+1)) < abs(n//2 - answer[0]):
            answer[0] = child_num

        return child_num + 1

    dfs(1, 0)
    return abs(answer[0]+1 - (n - (answer[0]+1)))

n, wires = 4, [[1, 2], [2, 3], [3, 4]]
print(solution(n, wires))
