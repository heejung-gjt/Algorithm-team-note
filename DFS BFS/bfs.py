from collections import deque


def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True


graph = [ # 각 노드가 연결된 정보를 표현한다 (2차원 리스트)
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9 # 각 노드가 방문된 정보를 표현한다 (1차원 리스트)
bfs(graph, 1, visited) # 정의된 DFS 함수를 호출한다