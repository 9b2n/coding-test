def solution(line):
    answer = []
    points = []
    
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            
            if a*d - b*c != 0:
                x = (b*f-e*d)/(a*d-b*c)
                y = (e*c-a*f)/(a*d-b*c)
                if x.is_integer() and y.is_integer():
                    points.append((int(x), int(y)))

    x_min, y_min = points[0]
    x_max, y_max = points[0]
    
    for x, y in points:
        x_max = max(x_max, x)
        x_min = min(x_min, x)
        y_max = max(y_max, y)
        y_min = min(y_min, y)

    for i in range(y_max, y_min-1, -1):
        string = ""
        for j in range(x_min, x_max+1):
            if (j, i) in points:
                string += "*"
            else:
                string += "."
        answer.append(string)

    return answer


line = 	[[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))
