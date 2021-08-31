### ? 스택이란 ?
스택은 후입선출(LIFO) 자료구조로 데이터를 추가할 때 맨 위에 추가하고 데이터를 꺼낼때 맨 위에 있는
 데이터를 꺼내는 방식이다. 즉 가장 최근에 들어간 자료가 가장 먼저 꺼내지는 구조이다.     
 
<br>

### 스택의 동작   
![stack](https://user-images.githubusercontent.com/64240637/107119454-fea76d80-68ca-11eb-9430-743b88841a13.PNG)    

__push__ : 데이터를 삽입하는 동작이다    
__pop__ : 스탣의 맨 위에 있는 데이터를 삭제하면서 반환하는 동작이다    

<br>

### 스택의 구현   
push(data) - data를 스택의 맨 위에 추가한다   
pop() - 스택에서 가장 위에 있는 데이터 제거한다    
peek() - 스택의 front 데이터를 반환한다 
empty() - 스택이 비워있는지 확인한다    

<br>

### ? 큐란 ?
큐는 선입선출(FIFO)자료구조로 제일 먼저 들어온 데이터가 가장 먼저 나가고 가장 늦게 들어온 데이터가
가장 늦게 나가는 구조이다.    
<br>

### 큐의 동작
![큐](https://user-images.githubusercontent.com/64240637/107120988-55b14080-68d3-11eb-8aff-24ea4e8c6e4a.png)      
   

인큐(enqueuer) : 데이터를 삽입하는 것   
디큐(dequeuer) : 데이터를 꺼내는 것    
<br>

### 큐의 구현
스택처럼 리스트를 이용하여 큐를 구현한다. 인큐는 append() 이용, 디큐는 pop()을 이용하였다   
```python
class Queue:
    def __init__(self):
        self.lists = []
        
    def enqueue(self,data):
        self.lists.append(data)
        print('push : ',data,end=' ')
        
        
    def dequeue(self):
        return self.lists.pop(0)
        
    def empty(self):
        if not self.lists:
            return True
        else:
            return False
    
    def peek(self):
        return self.lists[0]
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print('\n')

while not q.empty():
    print('pop :  ',q.dequeue(),end=' ')

"""
결과
push :  1 push :  2 push :  3 push :  4 push :  5 

pop :   1 pop :   2 pop :   3 pop :   4 pop :   5 
"""
```
데이터가 1,2,3,4,5 순으로 인큐했으르모 디큐할때는 먼저 들어온 1부터 차례대로 pop되는 것을 볼 수 있다

<br>

### 연결 리스트
링크를 이용해서 다음 순서의 자료를 구현하는 방식이다. 연결 리스트는 링크를 통해 다음 값을 알아내기 때문에 중간 값이 삭제되는 경우 링크만 바꿔주면 되는 장점이 있다. (파이썬에서 배열은 연결 리스트로 구현되어 있다)   

- 단순 연결 리스트 (singly linked list)   
단순 연결 리스트는 헤더 노드가 존재하고 헤더 노드는 다음 노드를 그리고 다음 노드는 그 다음 노드를 가리킨다. 즉 한 방향으로 연결되어 있기 때문에 단순 연결 리스트라고 부른다   

- 이중 연결 리스트
- 원형 연결 리스트 