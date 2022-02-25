def solution(x):
    arr = [0, 0, 1, 1]
    for i in range(4, x+1):
        arr.append(arr[i-1]+1)
        if not i%2:
            arr[i] = min(arr[i], arr[i//2]+1)
        if not i%3:
            arr[i] = min(arr[i], arr[i//3]+1)
    return arr[x]

print(solution(int(input())))
