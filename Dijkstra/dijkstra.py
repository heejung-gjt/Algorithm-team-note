import heapq
import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 출발노드까지의 거리가 0이도록 처음에 설정한다
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q) # q안에서 가장 최단 거리가 짧은 노드와 거리를 꺼낸다
        if distance[node] < dist: # 현재 꺼낸 노드의 거리값이 테이블에 기록되어 있는 값보다 크다면 이미 처리된것으로 간주 
            continue
        for i in graph[node]: # 현재 우선순위 큐에서 꺼낸 노드를 기준으로 해당 노드를 거쳐가는 경우를 확인하면 된다
            cost = dist + i[1] # i[0]은 인접한 노드를 말하고 i[1]은 거리값을 말한다
                               # 현재확인하고 있는 노드까지의 거리값 Dist에 그 노드와 인접한 다른 노드까지의 거리를 더한 값을 cost에 담는다 
            
            if cost < distance[i[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧을 경우 
                distance[i[0]] = cost # 현재 인접한 거리값distance[i[0]]보다 cost값이 더 작은경우 업데이트 해준다
                heapq.heappush(q, (cost, i[0])) # 값이 갱신될때마다 우선순위 큐에 해당 정보를 담아준다
                

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
    