n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
answer = arr[0]

def minValue(arr, i, j):
    return min(arr[i-1][(j-1)%3], arr[i-1][(j+1)%3]) + arr[i][j]

for i in range(1, n):
    for j in range(3):
        arr[i][j] = minValue(arr, i, j)

print(min(arr[n-1]))
