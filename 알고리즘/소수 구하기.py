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

(1) 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다 ex(10 -> 1,2,5,10)
(2) 2는 소수이므로 2(자기자신)을 제외한 2의 배수를 모두 지운다
(3) 남아있는 수 가운데 3(자기자신)을 제외한 3의 배수를 모두지운다
(4) 2~3번의 과정을 반복하면 해당하는 구간의 모든 소수가 남게 된다
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


"""
에라토스테네의 체와 차집합 이용한 소수구하기
"""

def solution(n):
  num = set(range(2, n + 1))

  for i in range(2, n + 1):
    if i in num:
      num -= set(range(2 * i, n + 1, i))

solution(10)