"""
1vs2, 2vs3, 3vs3, 3vs4, 4vs5
"""

arr = [1, 2, 3, 3, 4, 5]
answer = []
answer.append(arr[0])
for i in range(1, len(arr)):
    print(f'{arr[i - 1]} vs {arr[i]}')
