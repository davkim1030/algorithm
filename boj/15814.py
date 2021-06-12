s = input()
t = int(input())
for i in range(t):
	fr, to = map(int, input().split())
	fr, to = min(fr, to), max(fr, to)
	if fr == to:
		continue
	s = s[:fr] + s[to] + s[fr + 1:to] + s[fr] + s[to + 1:]
print(s)

