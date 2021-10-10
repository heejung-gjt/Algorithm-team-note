# list끼리 빼기

n1 = [1, 2, 3, 4, 5]
n2 = [2, 3, 5, 79, 89]

n1_sub_n2 = [x for x in n1 if x not in n2] 
print(n1_sub_n2) # 1, 4
