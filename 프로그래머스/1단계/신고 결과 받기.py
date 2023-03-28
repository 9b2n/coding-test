def solution(id_list, report, k):
    stop, reporter, history = {}, {}, set()
    for id in id_list:
        stop[id] = 0
        reporter[id] = set()

    for string in report:
        if string in history:
            continue
        history.add(string)
        f, t = string.split(" ")
        reporter[f].add(t)
        stop[t] += 1

    criminal = set([key if stop[key] >= k else '' for key in stop.keys()])
    criminal.remove('')

    return [len(list(reporter[id] & criminal)) for id in id_list]
