## 이진 탐색 알고리즘

- 순차 탐색: 리스트 안에 있는 특정한 __데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인__ 하는 방법

- 이진 탐색: 정렬되어 있는 리스트에서 __탐색 범위를 좁혀가며 데이터를 탐색__ 하는 방법  
  - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다

### 이진 탐색의 시간 복잡도

- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 __연산횟수는 log2N에 비례__ 하다
- ex) 초기 데이터 개수가 32개일때, 이상적으로 1단계를 거치면 16개 가량의 데이터만 남는다
    - 2단계를 거치면 8개 가량의 데이터가 남는다
    - 3단계를 거치면 4개 가량의 데이터가 남는다
- 즉, 이진 탐색은 탐색 범위를 절반씩, 줄이며, 시간 복잡도는 O(logN)을 보장한다    


<br>

### 이진 탐색 라이브러리
- bisect_left(a, x): __정렬된 순서를 유지__ 하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환한다    
- bisect_right(a, x): __정렬된 순서를 유지__ 하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환한다   

```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x)) # 2
print(bisect_right(a, x)) # 4
```
<br>

#### 이진 탐색 라이브러리 활용한 예제
```값이 특정 범위에 속하는 데이터 개수 구하기```   
```python
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4)) # 2
print(count_by_range(a, -1, 3)) # 6
```
<br>

### 파라메트릭 서치(Parametric Search)
파라메트릭 서치란 __최적화 문제를 결정 문제로 바꾸어 해결하는 기법__ 이다    
  - ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제

일반적으로 코테에서 파라메트릭 서치 문제는 __이진 탐색을 이용하여 해결__ 할 수 있다   

<br>

- 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이다. 예를 들어 데이터의 개수가 1000만개를 넘거나 탐색 범위의 크기가 1000억 이상이라면 이진 탐색 알고리즘을 사용해본다. 이때 입력 데이터의 개수가 많은 문제에는 input() 함수를 사용하면 동작속도가 느려 시간 초과로 오답 판정을 받을 수 있다   

#### 한 줄 입력받아 출력하는 코드
한 줄 입력받고 난 뒤 rstrip() 함수를 호출해야한다. readline()으로 입력하면 입력 후 엔터가 줄바꿈 기호로 입력되기 때문에 rstrip()함수를 사용하여 공백 문자를 제거한다   

```python
import sys

input_data = sys.stdin.readline().rstrip()

print(input_data)
```


- 이진탐색의 실제 구현은 어려운 작업이다. 코테에 단골로 나오는 문제이기 때문에 암기가 필요하다 !
