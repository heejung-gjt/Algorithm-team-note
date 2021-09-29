"""
완전탐색에서 많이 사용되는 라이브러리 combinations, permutations
"""


# 순열
from itertools import permutaitons

nums = [1, 2, 3, 4, 5]
result = list(permutaitons(nums))
result2 = list(permutaitons(nums, 3))


# 조합
from itertools import combinations

nums = [1, 2, 3, 4, 5]
result = list(combinations(nums, 3))
