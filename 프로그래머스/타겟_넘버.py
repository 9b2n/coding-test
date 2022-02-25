# def solution(numbers, target):
#     answer = 0
#     s = 0
#     answer = dfs(numbers, target, 0, '+', s) + dfs(numbers, target, 0, '-', s)
#     return answer

# def dfs (numbers, target, i, op, s):
#     if op == '+':
#         s += numbers[i]
#     else:
#         s -= numbers[i]
#     if i == len(numbers) - 1:
#         if s == target:
#             return 1
#         else:
#             return 0
#     return dfs(numbers, target, i+1, '+', s) + dfs(numbers, target, i+1, '-', s)

def solution(numbers, target):
    turn = 0
    return dfs(numbers,target,turn)

def dfs(numbers, target, turn):
    if turn == len(numbers):
        return 1 if sum(numbers)==target else 0
    a = dfs(numbers,target,turn+1)
    numbers[turn] = numbers[turn] * -1
    b = dfs(numbers,target,turn+1)
    return a + b

numbers, target = [1, 1, 1, 1, 1],	3
print(solution(numbers, target))
