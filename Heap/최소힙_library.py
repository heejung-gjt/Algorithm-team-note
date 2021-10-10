'''
�� ���̺귯�� ��� ���� : �ּ� ��
'''

import heapq

def heapsort(iterable): # �������� �� ����
    h = []
    result = []

    for value in iterable: # ��� ���Ҹ� ���ʴ�� ���� ����
        heapq.heappush(h, value)

    for i in range(len(h)): # ���� ���Ե� ��� ���Ҹ� ���ʴ�� ������ ���
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
