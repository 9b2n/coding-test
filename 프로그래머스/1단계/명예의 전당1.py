from heapq import heappush, heappop


def solution(k, score):
    answer = []
    h = []
    for s in score:
        heappush(h, s)
        if len(h) > k:
            heappop(h)
        answer.append(h[0])
    return answer
