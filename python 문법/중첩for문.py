# ���������� ����Ʈ �� ���ϱ� ���� ��ø for�� ���

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