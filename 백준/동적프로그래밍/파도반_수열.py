arr = [1, 1, 1, 2, 2]
for i in range(5, 100):
    arr.append(arr[i-5] + arr[i-1])

t = int(input())
for i in range(t):
    n = int(input())
    print(arr[n-1])
