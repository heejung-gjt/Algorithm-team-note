def dfs(graph, v, visited):
  visited[v] = True # 현재 노드를 방문 처리한다
  print(v, end=' ')
  for i in graph[v]: # 현재 노드와 연결된 다른 노드를 재귀적으로 방문한다
    if not visited[i]:
      dfs(graph, i, visited)


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
dfs(graph, 1, visited) # 정의된 DFS 함수를 호출한다