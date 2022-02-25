# def binarySearch(left, right, times, n):
#     result = right
#     while left <= right:
#         mid = (left+right)//2
#         cnt = 0

#         for time in times:
#             cnt += mid//time

#         if cnt >= n: 
#             if result > mid:
#                 result = mid
#             right = mid-1
#         else:
#             left = mid+1
            
#     return result

# def solution(n, times):
#     times.sort()
#     left = 0
#     right = times[-1] * n
#     answer = binarySearch(left, right, times, n)
#     return answer

def solution(n, times):
    left = 0
    right = times[-1] * n
    while left < right :
        left, right = binarySearch(left, right, n, times)
    return left

def binarySearch(left, right, n, times):
    mid = (left + right)//2
    cnt = 0

    for time in times:
        cnt += mid//time

    if cnt >= n:
        return left, mid
    else:
        return mid+1, right