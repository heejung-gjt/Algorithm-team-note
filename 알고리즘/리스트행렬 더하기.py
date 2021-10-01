# -*- coding: utf-8 -*-

"""
map과 lambda 이용해 구하기
"""
arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]
answer = []

for i in range(len(arr1)):
    for j in range(i, i + 1):
        arr = list(map(lambda x, y: x + y, arr1[i], arr2[j]))
        answer.append(arr)

print(answer) # [[4, 6], [7, 9]]


"""
zip함수 이용해 구하기
"""
arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]

print(answer) # [[4, 6], [7, 9]]
