n, k = map(int, input().split())
st = {}
for i in range(1, 7):
    st[i] = [0, 0]
for i in range(n):
    tmp = tuple(map(int, input().split()))
    st[tmp[1]][tmp[0]] += 1

room_cnt = 0
for g in st:
    for s in st[g]:
        room_cnt += s // k + (1 if s % k > 0 else 0)

print(room_cnt)

