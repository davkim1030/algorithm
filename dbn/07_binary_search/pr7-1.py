def bin_search(arr, target):
  start = 0
  end = len(arr) - 1
  while start <= end:
    mid = (start + end) // 2
    if target == arr[mid]:
      return mid
    if target < arr[mid]:
      end = mid - 1
    else:
      start = mid + 1
  return None


if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().strip().split()))
  m = int(input())
  to_find = list(map(int, input().strip().split()))

  arr.sort()
  for i in range(len(to_find) - 1):
    print("yes" if bin_search(arr, to_find[i]) else "no", end=' ')
  print("yes" if bin_search(arr, to_find[-1]) else "no")

