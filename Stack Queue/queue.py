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