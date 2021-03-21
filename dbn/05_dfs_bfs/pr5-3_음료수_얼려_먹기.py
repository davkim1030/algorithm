def dfs(field, visited, s_x, s_y):
  stack = [(s_x, s_y)]

  while stack:
    tmp = stack.pop()
    x, y = tmp
    visited[y][x] = True
    if y - 1 >= 0 and visited[y - 1][x] == False and field[y - 1][x] == 0:
      stack.append((x, y - 1))
    if x - 1 >= 0 and visited[y][x - 1] == False and field[y][x - 1] == 0:
      stack.append((x - 1, y))
    if y + 1 < len(field) and visited[y + 1][x] == False and field[y + 1][x] == 0:
      stack.append((x, y + 1))
    if x + 1 < len(field[0]) and visited[y][x + 1] == False and field[y][x + 1] == 0:
      stack.append((x + 1, y))
  return visited


if __name__ == "__main__":
  n, m = map(int, input().split())
  field = []
  visited = [[False for x in range(m)] for y in range(n)]
  cnt = 0

  for i in range(n):
    field.append(list(map(int, list(input()))))
  for y in range(n):
    for x in range(m):
      if visited[y][x] == False:
        visited[y][x] = True
        if field[y][x] == 0:
          visited = dfs(field, visited, x, y)
          cnt += 1
  print(cnt)

