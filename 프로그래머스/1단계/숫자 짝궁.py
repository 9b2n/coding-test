def solution(X, Y):
    answer = []
    listX, listY = list(X), list(Y)
    listX.sort()
    listY.sort()

    while listX and listY:
        if listX[-1] > listY[-1]:
            listX.pop()
        elif listX[-1] == listY[-1]:
            p = listX.pop()
            listY.pop()
            answer.append(p)
        else:
            listY.pop()

    r = "".join(answer) if answer else "-1"
    r = "0" if r[0] == "0" else r

    return r

X, Y = "100", "203045"
print(solution(X, Y))
