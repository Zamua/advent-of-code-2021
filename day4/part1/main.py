lines = list(filter(lambda line: line != "", [l.rstrip() for l in open("../in").readlines()]))
moves = list(map(int, lines[0].split(',')))
boards = [[list(map(int, line.split())) for line in lines[i:i+5]] for i in range(1, len(lines)-1, 5)]

def update_and_check(board, m):
    found_r, found_c, board_sum = None, None, 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == m:
                board[r][c], found_r, found_c = True, r, c
            elif board[r][c] != True:
                board_sum += board[r][c]

    if found_r is not None and found_c is not None:
        row_vals = [v == True for v in board[found_r]]
        col_vals = [board[i][found_c] == True for i in range(len(board))]

        if all(row_vals) or all(col_vals):
            return True, board_sum 

    return False, 0

for m in moves:
    for board in boards:
        is_won, board_sum = update_and_check(board, m)
        if is_won:
            print(board_sum*m)
            raise SystemExit
