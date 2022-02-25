def solution(rows, columns, queries):
    answer = []

    puzzle = [[i*columns + j+1 for j in range(columns)] for i in range(rows)]

    for x1, y1, x2, y2 in queries:
        save = puzzle[x1-1][y2-1]
        minV = float("inf")

        for yi in range(y2-1, y1-1, -1):
            puzzle[x1-1][yi] = puzzle[x1-1][yi-1]
            minV = min(minV, puzzle[x1-1][yi])

        for xi in range(x1-1, x2-1):
            puzzle[xi][y1-1] = puzzle[xi+1][y1-1]
            minV = min(minV, puzzle[xi][y1-1])

        for yi in range(y1-1, y2-1):
            puzzle[x2-1][yi] = puzzle[x2-1][yi+1]
            minV = min(minV, puzzle[x2-1][yi])

        for xi in range(x2-1, x1, -1):
            puzzle[xi][y2-1] = puzzle[xi-1][y2-1]
            minV = min(minV, puzzle[xi][y2-1])

        puzzle[x1][y2-1] = save
        minV = min(minV, save)

        answer.append(minV)

    return answer


rows, columns, queries = 6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
print(solution(rows, columns, queries))
