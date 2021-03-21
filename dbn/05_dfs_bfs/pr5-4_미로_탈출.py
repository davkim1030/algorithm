from collections import deque


def bfs(field):
  queue = deque()
  queue.append((0, 0))
  visited = [[False for x in range(m)] for y in range(n)]
  cnt = 0

  while queue:
    tmp = queue.popleft()
    x, y = tmp
    visited[y][x] = True
    if x == len(field[0]) - 1 and y == len(field) - 1:
      return cnt
    cnt += 1
    check = 0
    if y - 1 >= 0 and visited[y - 1][x] == False and field[y - 1][x] == 1:
      queue.append((x, y - 1))
    else:
      check += 1
    if x - 1 >= 0 and visited[y][x - 1] == False and field[y][x - 1] == 1:
      queue.append((x - 1, y))
    else:
      check += 1
    if y + 1 < len(field) and visited[y + 1][x] == False and field[y + 1][x] == 1:
      queue.append((x, y + 1))
    else:
      check += 1
    if x + 1 < len(field[0]) and visited[y][x + 1] == False and field[y][x + 1] == 1:
      queue.append((x + 1, y))
    else:
      check += 1
    if check == 4:
      cnt -= 1
  return cnt


if __name__ == "__main__":
  n, m = map(int, input().split())
  field = []

  for i in range(n):
    field.append(list(map(int, list(input()))))
  res = bfs(field)
  print(res)

