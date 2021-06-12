n = int(input())
c, s = 100, 100
for i in range(n):
	c_in, s_in = map(int, input().split())
	if c_in > s_in:
		s -= c_in
	elif c_in < s_in:
		c -= s_in
print(f'{c}\n{s}')

