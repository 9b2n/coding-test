n = int(input())
lines = list(map(int, input().split()))
lines.sort()
for i in range(1, n):
    lines[i] += lines[i-1]

print(sum(lines))
