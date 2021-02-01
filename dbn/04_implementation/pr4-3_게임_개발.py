def check_visited(v, x, y, h, w):
  if x < w - 1:
    if x > 0:
      if y < h - 1:
        if y > 0:
          return (v[y - 1][x - 1] and v[y - 1][x + 1]
            and v[y + 1][x - 1] and v[y + 1][x + 1])
        else:
          return (v[y + 1][x - 1] and v[y + 1][x + 1])
      else:
        return (v[y - 1][x - 1] and v[y - 1][x + 1])
    else:
      return (v[y - 1][x + 1] and v[y + 1][x + 1])
  else:
    return (v[y - 1][x - 1] and v[y + 1][x - 1])


def check_water(x, y, m, h, w):
  if x < w - 1:
    if x > 0:
      if y < h - 1:
        if y > 0:
          return (m[y - 1][x - 1] and m[y - 1][x + 1]
            and m[y + 1][x - 1] and m[y + 1][x + 1])
        else:
          return (m[y + 1][x - 1] and m[y + 1][x + 1])
      else:
        return (m[y - 1][x - 1] and m[y - 1][x + 1])
    else:
      return (m[y - 1][x + 1] and m[y + 1][x + 1])
  else:
    return (m[y - 1][x - 1] and m[y + 1][x - 1])


if __name__ == "__main__":
  h, w = map(int, input().strip().split())
  x, y, d = map(int, input().strip().split())
  m = [0 for i in range(h)]
  for i in range(h):
    m[i] = list(map(int, input().strip().split()))
  visited = [[m[i][j] == 1 for j in range(w)] for i in range(h)]
  cnt = 0

  while True:
    visited[y][x] = True
    cnt += 1
    d = (d - 1) % 4
    if d == 0 and y > 0 and visited[y - 1][x - 1] == False:
      y -= 1
    elif d == 1 and x < w - 1 and visited[y][x + 1] == False:
      x += 1
    elif d == 2 and y < h - 1 and visited[y + 1][x] == False:
      y += 1
    elif d == 3 and x > 0 and visited[y][x - 1] == False:
      x -= 1
    elif check_visited(visited, x, y, h, w) or check_water(x, y, m, h, w):
      if d == 0 and m[y + 1][x] == 0:
        y += 1
      elif d == 1 and m[y][x - 1] == 0:
        x -= 1
      elif d == 2 and m[y - 1][x] == 0:
        y -= 1
      elif d == 3 and m[y][x + 1] == 0:
        x += 1
      else:
        break
    else:
      cnt -= 1
      continue
  print(cnt)

