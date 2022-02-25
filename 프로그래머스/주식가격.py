from collections import deque
def solution(prices):
    result = deque([])

    for i in range(len(prices)-1,-1,-1):
        if not result :
            result.appendleft(len(result))
            continue
        
        cnt = 0
        for j in range(i+1,len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        result.appendleft(cnt)

    return list(result)

prices = [1,2,3,2,3,1]	
print(solution(prices))