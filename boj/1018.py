def get_cnt(x, y, arr):
    ss = 0
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            if arr[i][j] == 1:
                ss += 1
    return ss


m, n = list(map(int, input().split()))
board = []
c1 = [[0 for i in range(n)] for j in range(m)]
c2 = [[0 for i in range(n)] for j in range(m)]
for y in range(m):
    board.append(list(input()))
    if y % 2 == 0:
        for x in range(n):
            if x % 2 == 0:
                if board[y][x] == 'B':
                    c1[y][x] = 1
                else:
                    c2[y][x] = 1
            else:
                if board[y][x] == 'B':
                    c2[y][x] = 1
                else:
                    c1[y][x] = 1
    else:
        for x in range(n):
            if x % 2 == 0:
                if board[y][x] == 'B':
                    c2[y][x] = 1
                else:
                    c1[y][x] = 1
            else:
                if board[y][x] == 'B':
                    c1[y][x] = 1
                else:
                    c2[y][x] = 1
mm = m * n
for y in range(m - 7):
    for x in range(n - 7):
        tmp = get_cnt(x, y, c1)
        if mm > tmp:
            mm = tmp
        tmp = get_cnt(x, y, c2)
        if mm > tmp:
            mm = tmp
print(mm)

