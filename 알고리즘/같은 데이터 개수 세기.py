# 똑같은 데이터 개수 세기

# dictionary이용

def cnt_data(n):
    dic = {}
    for i in n:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic

cnt_data([1,1,2,3,4,5,6,6,6,7,8,8,8,8,8])  # {1: 3, 2: 2, 3: 2, 4: 2, 5: 2, 6: 4, 7: 2, 8: 6}


# count를 이용
def cnt_data(n):
    dic = {}
    for i in n:
        dic[i] = n.count(i)
    return dic

cnt_data([1,1,2,3,4,5,6,6,6,7,8,8,8,8,8])


# Counter를 이용

from collections import Counter

def cnt_data(n):
    dic = Counter(n)
    return  dic

cnt_data([1,1,2,3,4,5,6,6,6,7,8,8,8,8,8])
