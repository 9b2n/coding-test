n = int(input())
points = list(map(int, input().split()[:n]))

comPoints = sorted(list(set(points)))
dic = {comPoints[i]: i for i in range(len(comPoints))}

for point in points:
    print(dic[point], end=" ")
