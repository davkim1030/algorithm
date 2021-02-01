pos = input()
x, y = ord(pos[0]) - ord('a') + 1, int(pos[1])

cnt = 0
for i in [[0, -2], [2, 0], [0, 2], [-2, 0]]:
  d = 0 if i[0] == 0 else 1
  for j in [[1 if d == 0 else 0, 1 if d == 1 else 0], [-1 if d == 0 else 0, -1 if d == 1 else 0]]:
    if (1 <= x + i[0] + j[0] <= 8) and (1 <= y + i[1] + j[1] <= 8):
      cnt += 1
print(cnt)

