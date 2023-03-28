# 리팩토링 하면서 배운 것
# map()으로 각 할당 값 매핑
# 날짜 계산은 일(day)로 계산하면 간단하다.


def solution(today, terms, privacies):
    answer = []

    termInfo = {t.split()[0]: int(t.split()[1]) for t in terms}
    today = toDays(today)

    for idx, privacy in enumerate(privacies):
        date, t = privacy.split()
        past = toDays(date)
        target = past + termInfo[t] * 28
        if target - 1 < today:
            answer.append(idx+1)

    return answer


def toDays(date):
    y, m, d = map(int, date.split('.'))
    return y * 28 * 12 + m * 28 + d


today, terms, privacies = "2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))
