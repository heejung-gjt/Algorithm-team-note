n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for k in range(m):
  i, j = map(int, input().split())
  graph[i][j] = 1
  graph[j][i] = 1