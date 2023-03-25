def solution(lottos, win_nums):
    lottos, win_nums = set(lottos) - {0}, set(win_nums)
    correct = lottos & win_nums
    return [min(len(lottos) - len(correct) + 1, 6), min(6 - len(correct) + 1, 6)]


lottos, win_nums = [1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]
print(solution(lottos, win_nums))
