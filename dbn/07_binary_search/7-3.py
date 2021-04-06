"""
iterative binary search
"""
def binary_search(array, target):
  start = 0
  end = len(array)
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    if array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

if __name__ == "__main__":
  target = int(input("input a target integer: "))
  array = list(map(int, input("input integer values: ").strip().split()))
  array.sort()
  result = binary_search(array, target)
  print(result if result else "No such element in array")

