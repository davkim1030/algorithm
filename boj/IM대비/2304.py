n = int(input())
bars = []
X, Y = 0, 1

max_yi = 0
for i in range(n):
    bars.append(list(map(int, input().split())))
bars.sort(key=lambda x: x[X])
for i in range(n):
    if bars[i][Y] >= bars[max_yi][Y]:
        max_yi = i

size = 0
pre_h = 0
for i in range(0, max_yi + 1):
    h, w = 0, 0
    if i != max_yi:
        if pre_h < bars[i][Y]:
            h = bars[i][Y]
            pre_h = bars[i][Y]
        else:
            h = pre_h
        w = bars[i + 1][X] - bars[i][X]
        size += w * h
    else:
        size += bars[max_yi][Y]

pre_h = 0
for i in range(n - 1, max_yi, -1):
    h, w = 0, 0
    if pre_h < bars[i][Y]:
        h = bars[i][Y]
        pre_h = bars[i][Y]
    else:
        h = pre_h
    w = bars[i][X] - bars[i - 1][X]
    size += w * h
print(size)

