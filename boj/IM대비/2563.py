zone = [[0 for x in range(100)] for y in range(100)]
size = 0
n = int(input())
for _ in range(n):
    x1, y1 = map(int, input().split())
    for i in range(y1, y1 + 10):
        for j in range(x1, x1 + 10):
            size = size + 1 if zone[i][j] == 0 else size
            zone[i][j] = 1
print(size)

