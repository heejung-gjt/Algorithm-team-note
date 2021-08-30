# 순차적으로 리스트 값 비교하기 위해 중첩 for문 사용

def solution(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(nums[i], nums[j])
            
print(solution([6,10,2]))

'''
6 10
6 2
10 2
'''