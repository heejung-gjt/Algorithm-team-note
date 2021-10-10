'''
힙 라이브러리 사용 예제 : 최소 힙
'''

import heapq

def heapsort(iterable): # 오름차순 힙 정렬
    h = []
    result = []

    for value in iterable: # 모든 원소를 차례대로 힙에 삽입
        heapq.heappush(h, value)

    for i in range(len(h)): # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
