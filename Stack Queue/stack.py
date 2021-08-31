class Stack:
    def __init__(self):
        self.lists = []
    
    def push(self, data):
        print('push : ',data,end=' ')
        self.lists.append(data)
        
    def pop(self):
        return self.lists.pop()
    
    def empty(self):
        if not self.lists:
            return True
        else:
            return False
    
    def peek(self):
        return self.lists[-1]
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print('\n')

while not s.empty():
    data = s.pop()
    print('pop :  ',data,end=' ')