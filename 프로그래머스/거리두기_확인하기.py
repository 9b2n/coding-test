def solution(places):
    answer = []
    for i in range(5):
        room = ["OOOOOOO"]
        for j in range(5):
            room.append("O"+places[i][j]+"O")
        room.append("OOOOOOO")
        answer.append(check(room))
    return answer

def check(room):
    r = [[0 for _ in range(7)] for _ in range(7)]
    for i in range(1,6):
        for j in range(1,6):
            if room[i][j] == 'P':
                r[i][j] -= 1
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if room[i+x][j+y] != 'X':
                        r[i+x][j+y] -= 1
                        if r[i+x][j+y] <= -2:
                            return 0
    return 1

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
