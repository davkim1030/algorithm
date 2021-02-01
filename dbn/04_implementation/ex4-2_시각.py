def gen_tstr(h, m, s):
  res = str(h) if h >= 10 else "0" + str(h)
  res += str(m) if m >= 10 else "0" + str(m)
  res += str(s) if s >= 10 else "0" + str(s)
  return res


if __name__ == "__main__":
  n = int(input())
  cnt = 0
  for h in range(n + 1):
    for m in range(60):
      for s in range(60):
        if '3' in gen_tstr(h, m, s):
          cnt += 1
  print(cnt)

