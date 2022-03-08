h, m = map(int,input().split())
x = int(input())

print((h + (x + m) // 60) % 24, (x + m) % 60)
