zone = [[0 for x in range(100)] for y in range(100)]
size = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            size = size + 1 if zone[i][j] == 0 else size
            zone[i][j] = 1
print(size)

