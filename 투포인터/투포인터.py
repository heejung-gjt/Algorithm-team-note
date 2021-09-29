
n, m = map(int, input().split())
data = [*map(int, input().split())]
cnt = 0
inter_sum = 0
end = 0

for start in range(n):
    while inter_sum < m and end < n:
        inter_sum += data[end]
        end += 1
    if inter_sum == m:
        cnt += 1
    inter_sum -= data[start]
print(cnt)
