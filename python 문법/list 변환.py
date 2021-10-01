# -*- coding: utf-8 -*-

"""
정수형 123 리스트로 변환
"""

num = 123
n_list = [int(i) for i in str(num)]

print(n_list) # [1, 2, 3]


"""
map이용하기
"""

num = 123
print(map(int, str(num))) # [1, 2, 3]