def solution(n):
    arr = [0, 0, 0, 1, 0, 1]

    for i in range(6, n+1):
        if arr[i-5]:
            arr.append(arr[i-5] + 1)
        elif arr[i-3]:
            arr.append(arr[i-3] + 1)
        else:
            arr.append(0)
            
    return arr[n] if arr[n] else -1

print(solution(int(input())))
