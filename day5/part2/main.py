coords = list(filter(lambda c: c[0][0] == c[1][0] or c[0][1] == c[1][1] or abs(c[0][0] - c[1][0]) == abs(c[0][1] - c[1][1]), [list(map(lambda c: list(map(int, c.split(','))), coord)) for coord in [line.rstrip().split(" -> ") for line in open("../in").readlines()]]))
max_dimension = max(sum(sum(coords, []), [])) + 1
board = [[0]*max_dimension for _ in range(max_dimension)]
for ca, cb in coords:
    cax, cay, cbx, cby = *ca, *cb
    if cay == cby:
        left, right = sorted([cax, cbx])
        for x in range(left, right+1):
            board[cay][x] += 1
    elif cax == cbx:
        left, right = sorted([cay, cby])
        for y in range(left, right+1):
            board[y][cax] += 1
    elif abs(cax - cbx) == abs(cay - cby):
        left, right = sorted([(cax, cay), (cbx, cby)])
        lx, ly, rx, ry = *left, *right
        for i in range(rx+1 - lx):
            board[ly+i if ly<ry else ly-i][lx+i] += 1

print(sum([sum([1 for v in row if v>1]) for row in board]))
