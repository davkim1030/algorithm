n, m = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2
  for x in arr:
    if x > mid:
	  total += x - mid
  if total < m:
    end = mid - 1
  else:
    result = mid
	start = mid + 1

print(result)

