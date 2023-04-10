def solution(n):
    answer = []

    def hanoi(s, t, m, n):
        if n == 1:
            answer.append([s, t])
        else:
            hanoi(s, m, t, n - 1)
            hanoi(s, t, m, 1)
            hanoi(m, t, s, n - 1)

    hanoi(1, 3, 2, n)

    return answer
