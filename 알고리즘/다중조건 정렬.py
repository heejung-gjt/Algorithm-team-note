# lambda�Լ� �̿��ؼ� ���� ����Ʈ �ε������� �����ϴ� ��Һ��� �����ϱ�
# ���� ���� �����ϱ�

def solution(num):
    num = list(map(str, num))
    print(num)
    num.sort(key = lambda x : x*3, reverse = True) # lambda x: x*3�� num ���� ������ ���ڿ��� 3�� �ݺ��Ѵٴ� ��
    print(num) # ���ڿ� �񱳴� �ƽ�Ű�ڵ� ������ ġȯ�Ǿ� ���ĵȴ� .
    # 666, 101010, 222�� ù��° �ε��������� �񱳸� ���ش�. 6=86, 1=81, 2=82�̹Ƿ� 6>2>1���̴�
    return str(int(''.join(num)))
print(solution([6,10,2]))


#  ������ �ε������� �����ϴ� ������ ��������/�������� �����Ѵ�
n = int(input())
std_list = [list(map(str, input().split()))for _ in range(n)]
c = sorted(std_list, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for std in c:
    print(std[0])