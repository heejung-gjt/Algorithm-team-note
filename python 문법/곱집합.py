# 곱집합은 여러 집합들 간에 하나씩 뽑아 조합을 만들 수 있는 모든 수를 말한다

from itertools import product

a = [1,2,3]
b = ['a', 'b', 'c']

a = product(a,b)
print(list(a))

# [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]
