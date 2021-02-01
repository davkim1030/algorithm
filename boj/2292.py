if __name__ == "__main__":
  n = int(input())
  if n == 1:
    print(1)
  else:
    st = 1
    before = 1
    while True:
      if before < n <= before + 6 * st:
        print(st + 1)
        break
      before = before + 6 * st
      st += 1

