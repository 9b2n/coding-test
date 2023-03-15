def solution(num, total):
    answer = [0] * num
    minus = plus = center = total // num

    centerIdx = num // 2 if num % 2 else num // 2 - 1
    answer[centerIdx] = center

    for idx in range(centerIdx-1, -1, -1):
        answer[idx] = minus - 1
        minus -= 1

    for idx in range(centerIdx + 1, num):
        answer[idx] = plus + 1
        plus += 1

    return answer
