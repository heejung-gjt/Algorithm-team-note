def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2 # 중간점 인덱스 반환
    if array[mid] == target: 
        return mid
    elif array[mid] > target: # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인 
        return binary_search(array, target, start, mid - 1)
    else: # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split())) # 원소의 개수 n과 target을 입력받기
array = list(map(int, input().split())) # 전체 원소 입력받기

result = binary_search(array, target, 0, n - 1) # 이진 탐색 수행 결과 출력
if result == None:
    print('원소 존재 x')
else:
    print(result + 1)