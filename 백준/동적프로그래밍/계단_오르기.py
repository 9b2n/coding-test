n = int(input())
stairs = [int(input()) for _ in range(n)]
arr = []

if n < 3:
    print(sum(stairs))
else:
    arr.append(stairs[0])
    arr.append(stairs[0]+stairs[1])
    arr.append(max( stairs[0]+stairs[2], stairs[1]+stairs[2]))

    for i in range(3, n):
        arr.append(max(arr[i-2]+stairs[i], arr[i-3]+stairs[i-1]+stairs[i]))

    print(arr.pop())
