def solution(money):
    zero = [money[0], money[0]]
    first = [0, money[1]]

    for i in range(2,len(money) - 1):
        zero.append(max(zero[i-2] + money[i], zero[i-1]))
    
    for i in range(2,len(money)):
        first.append(max(first[i-2] + money[i], first[i-1]))

    return max(zero[-1],first[-1])