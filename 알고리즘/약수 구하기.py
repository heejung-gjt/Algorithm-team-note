'''
단순한 풀이 : for문을 돌면서 약수인지 아닌지 체크
O(N)의 시간복잡도를 갖는다
'''

def get_measure(n):
  num_list = []

  for i in range(1, n + 1):
    if n % i == 0:
      num_list.append(i)
  return num_list


'''
제곱근 활용한 풀이 : 자연수 N의 제곱근까지의 약수를 구하면 그 짝이 되는 약수가 자동으로 구해진다
O(N ^ (1/2))의 시간복잡도를 갖는다
'''

def get_measure(n):
  num_list = []

  for i in range(1, int(n ** (1 / 2)) + 1):
    if n % i == 0:
      num_list.append(i)
      if i**2 != n: # i != (n // i):
        num_list.append(n // i)
  num_list.sort()
  return num_list