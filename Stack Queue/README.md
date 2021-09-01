## 스택이란?

스택은 후입선출(LIFO) 자료구조로 데이터를 추가할 때 맨 위에 추가하고 데이터를 꺼낼때 맨 위에 있는 데이터를 꺼내는 방식이다. 즉 가장 최근에 들어간 자료가 가장 먼저 꺼내지는 구조이다.    

__list로 구현이 가능하기 때문에 굳이 링크드 리스트로 구현하지 않아도 된다__   
 

### 스택의 동작
![stack](https://user-images.githubusercontent.com/64240637/107119454-fea76d80-68ca-11eb-9430-743b88841a13.PNG)    

append : 데이터를 삽입하는 동작이다
pop : 스택의 맨 위에 있는 데이터를 삭제하면서 반환하는 동작이다 


### 스택의 구현
push(data) - data를 스택의 맨 위에 추가한다  
pop() - 스택에서 가장 위에 있는 데이터 제거한다   
peek() - 스택의 front 데이터를 반환한다   
empty() - 스택이 비워있는지 확인한다  

<br>

## 큐란 ?
큐는 선입선출(FIFO)자료구조로 제일 먼저 들어온 데이터가 가장 먼저 나가고 가장 늦게 들어온 데이터가 가장 늦게 나가는 구조이다.
  

### 큐의 동작
![?](https://user-images.githubusercontent.com/64240637/107120988-55b14080-68d3-11eb-8aff-24ea4e8c6e4a.png)      
   

인큐(enqueue) : 데이터를 삽입하는 것
디큐(dequeue) : 데이터를 꺼내는 것


### 큐의 구현
스택처럼 리스트를 이용하여 큐를 구현한다. 인큐는 append() 이용, 디큐는 pop(0)을 이용하였다. 큐를 리스트로 구현하는 것은 추천하지 않는다. pop(0), insert(0,a)는 o(n)의 시간복잡도를 갖는다

큐를 구현하는 3가지의 방법이 존재한다. 그중 deque를 사용하는 것을 추천한다

- collections의 deque (내부적으로 이중 연결 링크 리스트로 구현) append, popleft()사용 

- 파이썬에서 제공하는 모듈인 Queue 구현,  put(), get() 사용

- 링크드 리스트로 구현

```python
from collections import deque


class Queue:
    def __init__(self):
        self.list = deque([])
        
    def enque(self, data):
        self.list.append(data)
    
    def deque(self):
        return self.list.popleft()
    
    def empty(self):
        if self.list is None:
            return True
        else:
            return False
        
    def peek(self):
        return self.list[0]
    
```

```python
import queue

class Queue:
    def __init__(self):
        self.q = queue.Queue()
        
    def enque(self, data):
        self.q.put(data)
        
    def deque(self):
        return self.q.get()
    
    def empty(self):
        if self.list is None:
            return True
        else:
            return False
        
    def peek(self):
        return self.list[0]    
```

```python
class LinkedListQueue:
    
    class Node:
        def __init__(self, data, n = None):
            self.data = data
            self.next = n
            
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, data):
        if self.front is None:
            self.front = self.Node(data)
            self.rear = self.front
        else:
            self.rear.next = self.Node(data)
            self.rear = self.rear.next

    def dequeue(self):
        del_data = self.front.data
        self.front = self.front.next
        print('pop?? ? ???', del_data)
        if self.front is None:
            self.rear = None
        return del_data
    
    def peek(self):
        return print(f'front? ?? ??? {self.front.data}')
    
    def empty(self):
        return self.front == None and self.rear == None
    
    
    def outputNode(self):
        link = self.front
        print('???? ? ???', end=' ')
        while link:
            print(link.data, end=' ')
            link = link.next

q1 = LinkedListQueue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print()
q1.outputNode()
print()
print()
print('front? ???? ???', q1.front.data)
print('rear? ???? ???', q1.rear.data)
print()
q1.outputNode()
print()
q1.dequeue()
print()
q1.outputNode()
print()
q1.dequeue()
print()
q1.outputNode()
print()
print()
q1.peek()
```


### 연결 리스트
링크를 이용해서 다음 순서의 자료를 구현하는 방식이다. 연결 리스트는 링크를 통해 다음 값을 알아내기 때문에 중간 값이 삭제되는 경우 링크만 바꿔주면 되는 장점이 있다. (파이썬에서 배열은 연결 리스트로 구현되어 있다)

단순 연결 리스트 (singly linked list)
단순 연결 리스트는 헤더 노드가 존재하고 헤더 노드는 다음 노드를 그리고 다음 노드는 그 다음 노드를 가리킨다. 즉 한 방향으로 연결되어 있기 때문에 단순 연결 리스트라고 부른다

이중 연결 리스트

원형 연결 리스트