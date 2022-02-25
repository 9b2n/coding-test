from math import sqrt
def sieve_of_eratosthenes(x):
    arr = [True] * x
    for i in range(2, int(sqrt(x))+1):
        if arr[i]:
            for j in range(i+i, x, i):
                arr[j] = False 