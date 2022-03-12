def isFactor(x, y):
    return False if y%x else True

def isMultiple(x, y):
    return False if x%y else True

while True:
    n, m = map(int, input().split())
    if not n and not m:
        break
    f = isFactor(n, m)
    m = isMultiple(n, m)
    if f:
        print('factor')
    elif m:
        print('multiple')
    else:
        print('neither')
