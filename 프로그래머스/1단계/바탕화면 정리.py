def solution(wallpaper):
    row = []
    col = []
    for ridx in range(len(wallpaper)):
        for cidx in range(len(wallpaper[ridx])):
            if wallpaper[ridx][cidx] == '#':
                row.append(ridx)
                col.append(cidx)

    return [min(row), min(col), max(row)+1, max(col)+1]


wallpaper = [".#...", "..#..", "...#."]
print(solution(wallpaper))
