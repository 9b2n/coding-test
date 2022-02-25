def solution(n):
    arr = [0, 1, 2, 4, 7]
    for i in range(5, n+1):
        arr.append(arr[i-3] + arr[i-2] + arr[i-1])
    return arr[n]

n = int(input())

for i in range(n):
    print(solution(int(input())))
