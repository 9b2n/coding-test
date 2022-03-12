def findKInNFactorial(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

n, m = map(int, input().split())
five = findKInNFactorial(n, 5) - findKInNFactorial(n-m, 5) - findKInNFactorial(m, 5)
two = findKInNFactorial(n, 2) - findKInNFactorial(n-m, 2) - findKInNFactorial(m, 2)
print(min(five, two))
