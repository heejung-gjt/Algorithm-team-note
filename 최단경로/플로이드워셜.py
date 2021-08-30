INF = int(1e9) # ������ �ǹ��ϴ� �� ����

n = int(input()) # ����� ����, ������ ���� �Է�
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2���� ����Ʈ�� ����� �������� �ʱ�ȭ

for a in range(1, n + 1): # �ڱ� �ڽſ��� �ڱ� �ڽ����� ���� ����� 0���� �ʱ�ȭ
  for b in range(1, n + 1):
    if a==b:
      graph[a][b] = 0

for _ in range(m): # �� ������ ���� ������ �Է¹޾�, �� ������ �ʱ�ȭ
  a, b, c = map(int, input().split()) # A���� B�� ���� ����� c��� ����
  graph[a][b] = c

for k in range(1, n + 1): # ��ȭ�Ŀ� ���� �÷��̵� ���� �˰����� ����
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1, n + 1): # ����� ����� ���
  for b in range(1, n + 1):
    if graph[a][b] == INF: # ������ �� ���� ���, �����̶�� ���
      print('INFINITY', end=' ')
    else: # ������ �� �ִ� ��� �Ÿ��� ���
      print(graph[a][b], end=' ')
    print()