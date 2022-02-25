def solution(arr):
    answer = arr[0]

    for i in arr:
        answer = lcm(answer, i)

    return answer

def gcd(a,b):
    return b if a%b == 0 else gcd(b, a%b)

def lcm(a, b):
    return a*b//gcd(a,b)

arr = [2, 2, 2, 4, 5]
print(solution(arr))
