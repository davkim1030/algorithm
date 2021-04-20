n = int(input())
token = list(map(int, input().split()))
st = [1]
for i in range(1, len(token)):
    st = st[:len(st) - token[i]] + [i + 1] + st[len(st) - token[i]:]
for s in st:
    print(s, end=' ')

