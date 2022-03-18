# from collections import defaultdict
# n = int(input())
# cards = list(map(int, input().split()))
# m = int(input())
# targets = list(map(int, input().split()))
# deck = defaultdict(int)

# for card in cards:
#     deck[card] += 1

# for target in targets:
#     print(deck[target], end=' ')


import sys
n = int(sys.stdin.readline().strip())
cards = sorted(list(map(int, sys.stdin.readline().strip().split())))
m = int(sys.stdin.readline().strip())
targets = list(map(int, sys.stdin.readline().strip().split()))

def binarySearch(num, bound):
    s, e = 0, n
    while(s < e):
        m = (s + e) // 2
        # 가장 왼쪽 위치 찾기
        if bound == 0:
            if cards[m] < num:
                s = m + 1
            else:
                e = m
        # 가장 오른쪽 위치 찾기
        else:
            if cards[m] <= num:
                s = m + 1
            else:
                e = m
    return e

result = []
for target in targets:
    result.append(binarySearch(target,1) - binarySearch(target,0))
print(*result)
