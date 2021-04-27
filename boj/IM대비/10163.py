x0, y0, x1, y1 = 0, 1, 2, 3


def count(zone, find):
    cnt = 0
    for i in range(len(zone)):
        for j in range(len(zone[0])):
            cnt = cnt + 1 if zone[i][j] == find else cnt
    return cnt


n = int(input())
rects = []
for i in range(n):
    tmp = list(map(int, input().split()))
    rects.append([tmp[0], tmp[1], tmp[0] + tmp[2], tmp[1] + tmp[3]])

max_x, max_y = 0, 0
for i in range(n):
    max_x = max(max_x, rects[i][x1])
    max_y = max(max_y, rects[i][y1])
area = [[0 for x in range(max_x)] for y in range(max_y)]

for i in range(n):
    for y in range(rects[i][y0], rects[i][y1]):
        for x in range(rects[i][x0], rects[i][x1]):
            area[y][x] = i + 1


for i in range(1, n + 1):
    print(count(area, i))

