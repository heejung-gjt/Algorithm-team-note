'''
1. O(n)의 시간복잡도를 가지는 소수판별 함수
'''

def is_prime(nums):
  for i in range(2, nums):
    if nums % i == 0:  # i로 나누어 떨어지면 소수가 아니므로 false리턴
      return False
  return True


'''
2. 약수의 특성을 활용한 소수판별 함수
약수의 중간값을 기준으로 한쪽을 검사한다. 약수가 존재하지 않으면 다른한쪽에도 약수가 존재하지
않는다
'''

import math

def is_prime(nums):
  for i in range(2, int(math.sqrt(nums) + 1)):
    if nums % i == 0:
      return False
  return True


'''
3. 특정수 nums가 주어진 상황이 아닌 여려 개의 수에 대해 소수 판별하는 함수

에라토스테네스체 알고리즘

(1) 2 ~ N까지의 범위가 담긴 배열을 만든다
(2) 해당 배열 내에 가장 작은 수 i부터 시작해 i의 배수들을 해당 배열에서 지운다
(3) 주어진 범위 내의 i의 배수가 지워진 후 i 다음으로 작은 수의 배수를 같은 방식으로 지운다
(4) 반복할 수 없을 때까지 2,3번의 과정을 반복한다
'''

def is_prime(nums):
  arr = [False, False] + [True] * (nums - 1)

  for i in range(2, nums + 1): 
    if arr[i]:
      for j in range(2 * i, nums + 1, i):
        arr[j] = False

  return arr


arr = is_prime(100)

for i in range(len(arr)):
  if arr[i] == True:
    print(i, end = ' ')