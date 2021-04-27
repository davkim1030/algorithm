def bingo_cnt(board):
    cnt = 0
    # case of horizontal bingo
    for y in range(len(board)):
        if board[y] == [0 for _ in range(len(board[0]))]:
            cnt += 1
    # case of vertical bingo
    for x in range(len(board[0])):
        zero_cnt = 0
        for y in range(len(board)):
            if board[y][x] == 0:
                zero_cnt += 1
            else:
                break
        if zero_cnt == len(board):
            cnt += 1
    # case of diagonal bingo left-up to right-down
    zero_cnt = 0
    for y in range(len(board)):
        if board[y][y] == 0:
            zero_cnt += 1
    if zero_cnt == len(board):
        cnt += 1
    # case of diagonal bingo left-down to right-up
    zero_cnt = 0
    for y in range(len(board)):
        if board[len(board) - y - 1][y] == 0:
            zero_cnt += 1
    if zero_cnt == len(board):
        cnt += 1
    return cnt


def find_value(board, find):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == find:
                board[y][x] = 0
                return


bingo = []
for i in range(5):
    bingo.append(list(map(int, input().split())))

call = []
for i in range(5):
    call.extend(list(map(int, input().split())))

for i in range(len(call)):
    find_value(bingo, call[i])
    if bingo_cnt(bingo) >= 3:
        print(i + 1)
        break

