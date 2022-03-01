n = int(input())
points = list(map(int, input().split()[:n]))
conPoints = sorted(list(set(points)))
for point in points:
    print(conPoints.index(point), end=" ")
