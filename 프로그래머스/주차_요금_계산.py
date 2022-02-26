from math import ceil
from collections import defaultdict

def solution(fees, records):
    answer = []
    dic = defaultdict(list)
    
    for record in records:
        time, number, io = record.split(' ')
        h, m = time.split(':')
        dic[number].append(int(h)*60 + int(m))
    
    dic = dict(sorted(dic.items()))

    for times in dic.values():
        result = 0
        for i in range(len(times)):
            if i%2:
                result += times[i]
            else:
                result -= times[i]
        if result <= 0:
            result += 23*60 + 59
        answer.append(calculateFee(fees, result))

    return answer

def calculateFee(fees, time):
    if time <= fees[0]:
        return fees[1]
    return fees[1] + ceil((time-fees[0])/fees[2])*fees[3]

fees, records = [1, 461, 1, 10], ["00:00 1234 IN"]
print(solution(fees, records))
