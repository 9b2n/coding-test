n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
nums = list(map(int, input().split()))

def divideNSearch(arr, l, r, num):
    while l <= r:
        m = (r + l) // 2
        if arr[m] == num:
            return 1
        elif arr[m] > num:
            r = m - 1
        else:
            l = m + 1
    return 0

for x in nums:
    print(divideNSearch(A, 0, n-1, x))
