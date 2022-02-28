from heapq import heapify, heappop

def solution(A, B):
    answer = 0
    heapify(A)
    heapify(B)

    a = 0
    b = 0
    while A and B:
        if not a and A:
            a = heappop(A)
        if not b and B:
            b = heappop(B)
            
        if a >= b:
            b = 0
        else:
            answer += 1
            a = 0
            b = 0
        
    return answer

A, B = 	[2, 2, 2, 2], [1, 1, 1, 1]
print(solution(A, B))
