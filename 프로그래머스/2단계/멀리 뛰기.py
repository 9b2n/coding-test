def solution(n):
    arr = [1, 1]

    for i in range(2, n+1):
        arr.append(arr[i-2] + arr[i-1])

    return arr[n] % 1234567

# 칸/방법 수
# 1/1
# 2/2
# 3/3
# 4/5
# 5/8
