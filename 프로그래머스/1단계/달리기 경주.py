def solution(players, callings):

    d = {name: idx for idx, name in enumerate(players)}

    for call in callings:
        idx = d[call]
        players[idx-1], players[idx] = players[idx], players[idx-1]
        d[players[idx-1]], d[players[idx]] = d[players[idx]], d[players[idx-1]]

    return players
