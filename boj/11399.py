n = int(input())
li = list(map(int, input().split(" ")))
li.sort()
s = 0
for i in range(1, n + 1):
    s = s + li.pop() * i
print(s)

