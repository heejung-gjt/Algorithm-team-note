'''
������ ���� ���
�ܰ踶�� �湮���� ���� ��� �߿��� �ִ� �Ÿ��� ���� ª�� ��带 �����ϱ� ����
�� �ڷᱸ���� �̿��Ѵ�
�ð����⵵ : O(ElogV)
���� �켱���� ť���� ���� ���� ����� �ٸ� ������ Ȯ���ϴ� �� Ƚ����
�ִ� ������ ����(E)��ŭ ������ ����� �� �ִ�
'''

import heapq
import sys


input = sys.stdin.readline
INF = int(1e9) # ������ �ǹ��ϴ� ������ 10���� ����

n, m = map(int, input().split()) # ����� ����, ������ ���� �Է¹ޱ�
start = int(input()) # ���� ��� ��ȣ �Է¹ޱ�
graph = [[] for i in range(n + 1)] # �� ��忡 ����Ǿ� �ִ� ��忡 ���� ������ ��� ����Ʈ �����
distance = [INF] * (n + 1) # �ִ� �Ÿ� ���̺��� ��� �������� �ʱ�ȭ

for _ in range(m): # ��� ���� ������ �Է¹ޱ�
  a, b, c = map(int, input().split()) # a�� ��忡�� b�� ���� ���� ����� C��� �ǹ�
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # ���� ���� ���� ���� �ִ� ��δ� 0���� �����Ͽ� ť�� ����
  distance[start] = 0

  while q: # ť�� ������� �ʴٸ�
    dist, now = heapq.heappop(q) # ���� �ִ� �Ÿ��� ª�� ��忡 ���� ���� ������
    if distance[now] < dist: # ���� ��尡 �̹� ó���� ���� �ִ� ����� ����
      continue

    for i in graph[now]: # ���� ��带 ���ļ�, �ٸ� ���� �̵��ϴ� �Ÿ��� �� ª�� ���
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start) # ���ͽ�Ʈ�� �˰����� ����

for i in range(1, n + 1): # ��� ���� ���� ���� �ִ� �Ÿ��� ���
  if distance[i] == INF: # ������ �� ���� ���, �����̶�� ���
    print('INFINITY')
  else: # ������ �� �ִ� ��� �Ÿ��� ���
    print(distance[i])