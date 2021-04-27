def get_h(exc, hs):
    size = 0
    for i in range(len(hs)):
        if i not in exc:
            size += hs[i]
    return size


hs = []
for i in range(9):
    hs.append(int(input()))

for i in range(len(hs) - 1):
    for j in range(i + 1, len(hs)):
        if get_h([i, j], hs) == 100:
            hs.pop(j)
            hs.pop(i)
            break
hs.sort()
for i in hs:
    print(i)

