n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
s = sum(a[-(n - k):])
s += sum(b[-k:])

print(s)

