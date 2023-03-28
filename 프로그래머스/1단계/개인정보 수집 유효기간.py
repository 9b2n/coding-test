from datetime import datetime


def solution(today, terms, privacies):
    answer = []
    y, m, d = today.split('.')
    y, m, d = int(y), int(m), int(d)
    termInfo = {t.split()[0]: int(t.split()[1]) for t in terms}
    days = [28] + [i for i in range(1, 29)]
    months = [12] + [i for i in range(1, 13)]

    for idx, privacy in enumerate(privacies):
        date, t = privacy.split()
        dy, dm, dd = date.split('.')
        dy, dm, dd = int(dy), int(dm), int(dd)

        td = days[dd - 1]
        tm = months[dm + (dd - 2) // 28]
        ty = dy + (dm + (dd - 2) // 28 - 1) // 12

        x = tm + termInfo[t]
        tm = months[x % 12]
        ty = ty + (x - 1)//12

        if isPast(ty, tm, td, y, m, d):
            answer.append(idx + 1)

    return answer


def isPast(ty, tm, td, y, m, d):
    return datetime(ty, tm, td) < datetime(y, m, d)


today, terms, privacies = "2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))
