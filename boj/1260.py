def dfs(arr, start, n):
	stack = [start]
	visited = []

	while stack:
		tmp = stack.pop()
		if tmp not in visited:
			visited.append(tmp)
			print(tmp, end=' ')
		for i in range(n, 0, -1):
			if arr[tmp][i] and i not in visited:
				stack.append(i)
	print()

def bfs(arr, start, n):
	queue = [start]
	visited = []

	while queue:
		tmp = queue.pop(0)
		if tmp not in visited:
			visited.append(tmp)
			print(tmp, end=' ')
		for i in range(1, n + 1):
			if arr[tmp][i] and i not in visited:
				queue.append(i)
	print()


if __name__ == "__main__":
	n, m, v = map(int, input().strip().split())
	arr = [[False for _ in range(n + 1)] for a in range(n + 1)]
	for _ in range(m):
		a, b = map(int, input().strip().split())
		arr[a][b] = arr[b][a] = True
	dfs(arr, v, n)
	bfs(arr, v, n)

