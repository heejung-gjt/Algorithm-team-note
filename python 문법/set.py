# -*- coding: utf-8 -*-

n_list = [1, 1, 2, 3, 4, 4]
set1 = set(n_list) # set([1, 2, 3, 4])

"""
교집합, 합집합, 차집합에 이용가능
"""

# 교집합
set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,8,9])
print(set1 & set2) # set([3, 4, 5, 6])
print(set1.intersection(set2)) #set([3, 4, 5, 6])


# 차집합
set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,8,9])
print(set1 - set2) # set([1, 2])
print(set1.difference(set2)) #set([1, 2])


# 합집합
set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,8,9])
print(set1 | set2) # set([1, 2, 3, 4, 5, 6, 8, 9])
print(set1.union(set2)) # set([1, 2, 3, 4, 5, 6, 8, 9])
