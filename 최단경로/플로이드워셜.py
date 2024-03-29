INF = int(1e9) # 무한을 의미하는 값 설정

n = int(input()) # 노드의 개수, 간선의 개수 입력
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2차원 리스트를 만들고 무한으로 초기화

for a in range(1, n + 1): # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
  for b in range(1, n + 1):
    if a==b:
      graph[a][b] = 0

for _ in range(m): # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
  a, b, c = map(int, input().split()) # A에서 B로 가는 비용은 c라고 설정
  graph[a][b] = c

for k in range(1, n + 1): # 점화식에 따라 플로이드 워셜 알고리즘을 수행
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1, n + 1): # 수행된 결과를 출력
  for b in range(1, n + 1):
    if graph[a][b] == INF: # 도달할 수 없는 경우, 무한이라고 출력
      print('INFINITY', end=' ')
    else: # 도달할 수 있는 경우 거리를 출력
      print(graph[a][b], end=' ')
    print()