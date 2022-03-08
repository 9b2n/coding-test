x, y, z = map(int, input().split())

if x == z == y:
    print(10000 + x*1000)
elif x == z or x == y:
    print(1000 + x * 100)
elif  y == z:
    print(1000 + y * 100)
else:
    print(max(x, y, z)*100)
