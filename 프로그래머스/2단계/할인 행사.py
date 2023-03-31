def solution(want, number, discount):
    answer = 0
    compare = set(want)

    d = {want[i]: number[i] for i in range(len(want))}

    for idx in range(len(discount)):
        if discount[idx - 10] in compare and idx > 9:
            d[discount[idx - 10]] += 1

        if discount[idx] in compare:
            d[discount[idx]] -= 1

        flag = 1
        for v in d.values():
            if v > 0:
                flag = 0
                break

        if flag:
            answer += 1

    return answer


want, number, discount = ["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple",
                                                                                       "banana", "rice", "apple",
                                                                                       "pork", "banana", "pork", "rice",
                                                                                       "pot", "banana", "apple",
                                                                                       "banana"]
print(solution(want, number, discount))
