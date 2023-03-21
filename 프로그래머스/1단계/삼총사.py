from itertools import combinations


def solution(number):
    return sum([sum(couple) == 0 for couple in list(combinations(number, 3))])
