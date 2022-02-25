def solution(n, left, right):
    answer = []
    for i in range(1,n+1):
        if left >= n * (i-1) and left < n * i:
            row = [i] * i
            for j in range(i+1, n+1):
                row.append(j)
            answer.extend(row[left - n * (i-1):right- n * (i-1) + 1])
        elif left < n * (i-1) and len(answer) < right - left + 1:
            row = [i] * i
            for j in range(i+1, n+1):
                row.append(j)
            answer.extend(row[:right - n * (i-1) + 1])
        else:
            continue
    
    return answer

def solution2(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer

n, left, right = 4, 1, 3
print(solution(n, left, right))
