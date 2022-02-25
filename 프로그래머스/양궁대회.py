def solution(n, info):
    maxDiff, maxArr = 0, [-1]

    def dfs(arr, idx, n):
        nonlocal maxDiff, maxArr
        if idx > 10:
            if not n:
                arr[10] = n
            diff = diffScore(info, arr)
            if diff <= 0:
                return
            arr[10] = n
            if maxDiff < diff:
                maxDiff = diff
                print(maxDiff, maxArr, arr)
                maxArr = arr[:]
            elif maxDiff == diff:
                for i in range(11):
                    if maxArr[10-i] > arr[10-i]:
                        break
                    elif maxArr[10-i] < arr[10-i]:
                        maxArr = arr[:]
                        break
            return

        if info[idx] < n:
            arr[idx] = info[idx] + 1
            dfs(arr, idx+1, n-info[idx]-1)
            arr[idx] = 0
        dfs(arr, idx+1, n)
    
    dfs([0] * 11, 0, n)

    return maxArr

def diffScore(aList, lList):
    aScore, lScore = 0, 0
    for i in range(10):
        if aList[i] < lList[i]:
            lScore += 10-i
        elif aList[i] > lList[i]:
            aScore += 10-i
        elif aList[i] != 0:
            aScore += 10-i
    return lScore - aScore

n, info = 9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
print(solution(n, info))
