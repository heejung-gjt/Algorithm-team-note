from collections import deque


n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

def dfs(v):
    visited[v] = 1
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    visited[v] = 1
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in range(1, n + 1):
            if visited[v] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1


for k in range(m):
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

cnt = 0
for i in range(n + 1):
    if visited[i] == 0:
        dfs(i) # bfs(i)
        cnt += 1

print(cnt)