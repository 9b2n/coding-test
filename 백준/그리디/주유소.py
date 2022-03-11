n = int(input())
roads = list(map(int, input().split()))
olis = list(map(int, input().split()))

curPrice = olis[0]
partialSub = roads[0]
result = 0

for i in range(1, len(olis)-1):
    if olis[i] < curPrice:
        result += curPrice*partialSub
        partialSub = roads[i]
        curPrice = olis[i]
    else:
        partialSub += roads[i]

print(result + partialSub*curPrice)
