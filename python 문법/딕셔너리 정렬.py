d = {1:3, 2:5, 3:-1, 4:23}

# sorted를 이용한 정렬
print(sorted(d)) # [1, 2, 3, 4]

# key값 기준으로 정렬
print(sorted(d.keys(), key = lambda x: x)) # [1, 2, 3, 4]


# value값 기준으로 정렬
print(sorted(d.values(), key = lambda x : x)) # [-1, 3, 5, 23]

# items()를 이용한 정렬
print(sorted(d.items(), key=lambda x : x[0])) # [(1, 3), (2, 5), (3, -1), (4, 23)]
print(sorted(d.items(), key=lambda x : x[1])) # [(3, -1), (1, 3), (2, 5), (4, 23)]
