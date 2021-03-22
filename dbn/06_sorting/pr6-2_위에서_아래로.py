n = int(input())
arr = list()
for i in range(n):
  arr.append(int(input()))

arr.sort(reverse=True)

for i in range(n - 1):
  print(arr[i], end=' ')
print(arr[-1])

