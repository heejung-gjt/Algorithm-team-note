array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end:
    return
  pivot = start
  left = start + 1 # 가장 왼쪽 값
  right = end # 가장 오른쪽 값
  while(left <= right): # 두 값이 엇갈릴때까지 반복

    # 피벗보다 큰 데이터를 찾을때까지 반복한다
    while(left <= end and array[left] <= array[pivot]):
      left += 1

    # 피벗보다 작은 데이터를 찾을 때까지 반복한다
    while(right > start and array[right] >= array[pivot]):
      right -= 1
    # 엇갈렸다면 작은 데이터와 피벗을 교체한다
    if(left > right):
      array[right], array[pivot] = array[pivot], array[right]
    # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체한다
    else:
      array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행한다
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

  quick_sort(array, 0, len(array) - 1)
  

# 파이써닉한 퀵 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  if len(array) <= 1:
    return array
  pivot = array[0] # 피벗은 첫번째 원소
  tail = array[1:] # 피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)






















