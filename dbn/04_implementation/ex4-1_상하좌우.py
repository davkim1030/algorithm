n = int(input())
path = input().strip().split()
x, y = 1, 1

for d in path:
  if d == 'L':
    x = x if x <= 1 else x - 1
  elif d == 'R':
    x = x if x >= n else x + 1
  elif d == 'U':
    y = y if y <= 1 else y - 1
  else:
    y = y if y >= n else y + 1
print(y, x)
