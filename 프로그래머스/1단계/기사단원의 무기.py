from math import sqrt


def solution(number, limit, power):
    answer = []
    for i in range(1, number + 1):
        n = numOfDivisors(i)
        answer.append(n if n <= limit else power)

    return sum(answer)


def numOfDivisors(n):
    num = 0
    for i in range(1, int(sqrt(n)) + 1):
        if not n % i:
            num += 1 if i ** 2 == n else 2

    return num
