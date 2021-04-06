"""
recursive binary search
"""
def binary_search(array, target, start, end):
  if start > end:
    return None;
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return (binary_search(array, target, start, mid - 1))
  return (binary_search(array, target, mid + 1, end))


if __name__ == "__main__":
  target = int(input("input a target integer: "))
  array = list(map(int, input("input integer values: ").strip().split()))
  array.sort()
  result = binary_search(array, target, 0, len(array) - 1)
  print(result if result else "No such element in array")

