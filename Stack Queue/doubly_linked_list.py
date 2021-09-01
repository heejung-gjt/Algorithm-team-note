class DoublyLinkedList:
    
    class Node:
        def __init__(self, v, n = None, p = None):
            self.value = v
            self.next = n
            self.prev = p
        
        
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertNodeFront(self, data): # 삽입
        if self.head is None:
            self.head = self.Node(data)
            self.tail = self.head
        else:
            self.head.prev = self.Node(data, n=self.head) # 기존 노드의 prev
            self.head = self.head.prev
    
    def insertNodeBack(self, data):
        if self.tail is None:
            self.tail = self.Node(data)
            self.head = self.tail
        else:
            self.tail.next = self.Node(data, p=self.tail)
            self.tail = self.tail.next
            
    def outputNodeFront(self): # 출력
        if self.head is None:
            print('x')
            return
        else:
            print('\n데이터 출력')
            link = self.head
            while link:
                print(link.value, '<->', end = ' ')
                link = link.next
    
    def outputNodeBack(self):
        if self.tail is None:
            print('x')
            return
        else:
            print('데이터 출력')
            link = self.tail
            while link:
                print(link.value, '<->', end = ' ')
                link = link.prev
            return
    
    def deleteNodeFront(self): # 삭제
        if self.head is None:
            print('노드 존재하지 않는다')
            return
        else:
            print(f'{self.head.value} 데이터 삭제')
            self.head = self.head.next
            if self.head is None:
              print(self.head.prev,'ddd')
              self.head = None
              return 
            self.head.prev = None
    
    def deleteNodeBack(self):
        if self.tail is None:
            print('x')
            return
        else:
            print(f'{self.tail.value} 데이터 삭제')
            self.tail = self.tail.prev
            self.tail.next = None
            
    def searchNodeFront(self, data): # 탐색
        if self.head is None:
            print('x')
            return
        else:
            link = self.head
            index = 0
            while link:
                if link.value == data:
                    return index
                else:
                    link = link.next
                    index += 1
                    
    def searchNodeBack(self, data):
        if self.tail is None:
            print('x')
            return
        else:
            link = self.tail
            index = 0
            
            while link:
                if link.value == data:
                    return index
                else:
                    link = link.prev
                    index -= 1

    def emptyNode(self): # 노드 존재 확인
        if self.head is None:
            print('해당 노드는 비워져 있습니다')
            return True
        else:
            print('해당 노드는 존재합니다')
            return False

    def peekNodeFront(self): # Front, rear 데이터 확인
        if self.head is None:
            print('노드가 존재하지 않습니다')
        else:
            return print(f'front에 존재하는 데이터 {self.head.value}')
    
    def peekNodeBack(self):
        if self.tail is None:
            print('노드가 존재하지 않습니다')
        else:
            return print(f'back에 존재하는 데이터 {self.tail.value}')
