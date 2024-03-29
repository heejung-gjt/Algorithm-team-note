'''
개선된 구현 방법
단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해
힙 자료구조를 이용한다
시간복잡도 : O(ElogV)
현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총 횟수는
최대 간선의 개수(E)만큼 연산이 수행될 수 있다
'''

import heapq
import sys


input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n, m = map(int, input().split()) # 노드의 개수, 간선의 개수 입력받기
start = int(input()) # 시작 노드 번호 입력받기
graph = [[] for i in range(n + 1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
distance = [INF] * (n + 1) # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m): # 모든 간선 정보를 입력받기
  a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 C라는 의미
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
  distance[start] = 0

  while q: # 큐가 비어있지 않다면
    dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
      continue

    for i in graph[now]: # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start) # 다익스트라 알고리즘을 수행

for i in range(1, n + 1): # 모든 노드로 가기 위한 최단 거리를 출력
  if distance[i] == INF: # 도달할 수 없는 경우, 무한이라고 출력
    print('INFINITY')
  else: # 도달할 수 있는 경우 거리를 출력
    print(distance[i])