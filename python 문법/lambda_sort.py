# lambda함수 이용해서 다중 리스트 인덱스값에 존재하는 요소별로 정렬하기
# 다중 조건 정렬하기

def solution(num):
    num = list(map(str, num))
    print(num)
    num.sort(key = lambda x : x*3, reverse = True) # lambda x: x*3은 num 인자 각각의 문자열을 3번 반복한다는 뜻
    print(num) # 문자열 비교는 아스키코드 값으로 치환되어 정렬된다 .
    # 666, 101010, 222의 첫번째 인덱스값으로 비교를 해준다. 6=86, 1=81, 2=82이므로 6>2>1순이다
    return str(int(''.join(num)))
print(solution([6,10,2]))


#  각각의 인덱스값에 존재하는 값들을 내림차순/오름차순 정렬한다
n = int(input())
std_list = [list(map(str, input().split()))for _ in range(n)]
c = sorted(std_list, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for std in c:
    print(std[0])