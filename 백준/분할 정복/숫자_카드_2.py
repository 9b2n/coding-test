from collections import defaultdict
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
deck = defaultdict(int)

for card in cards:
    deck[card] += 1

for target in targets:
    print(deck[target], end=' ')
