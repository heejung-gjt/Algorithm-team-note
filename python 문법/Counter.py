# most_common()메서드 : 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는 메서드

from collections import Counter

def cnt_data(n):
    dic = Counter(n).most_common()
    return  dic

cnt_data([1,1,2,3,4,5,6,6,6,7,8,8,8,8,8])

# [(8, 5), (6, 3), (1, 2), (2, 1), (3, 1), (4, 1), (5, 1), (7, 1)]
