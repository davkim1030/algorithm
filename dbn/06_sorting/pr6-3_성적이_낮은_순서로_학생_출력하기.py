n = int(input())
students = []

for i in range(n):
  name, score = input().split()
  students.append((name, int(score)))

students.sort(key=lambda x: x[1])

for i in range(n - 1):
  print(students[i][0], end=' ')
print(students[-1][0])

