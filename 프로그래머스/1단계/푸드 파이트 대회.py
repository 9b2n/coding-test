def solution(food):
    arr = [str(i) * (food[i] // 2) for i in range(1, len(food))]
    return "".join(arr) + "0" + "".join(sorted(arr, reverse=True))
