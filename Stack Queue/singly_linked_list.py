class SinglyLinkedList:
    
    class Node:
        def __init__(self, v, n = None):
            self.value = v
            self.next = n
            
    def __init__(self):
        self.head = None

    def insertNode(self, data):
        if self.head is None:
            print('�߰��Ǵ� ������>>>', data)
            self.head = self.Node(data)
        else:
            print('�߰��Ǵ� ������>>>', data)
            self.head = self.Node(data, self.head)

    def outputNode(self):
        if self.head is None:
            print('����� ��尡 �����ϴ�')
            print()
            return
        else:
            link = self.head
            print()
            print('��µǴ� ���>>>>', end= ' ')
            while link:
                print(link.value, end=' ')
                link = link.next
            print()
            print()
            
    def deleteNode(self):
        if self.head is None:
            print('������ ��尡 �����ϴ�')
            return
        else:
            print('�����Ǵ� ��� : ', self.head.value)
            self.head = self.head.next

    def searchNode(self, data):
        if self.head is None:
            print('ã���� �ִ� ��尡 �����ϴ�')
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
            print(f'ã���ô� {data} �����ʹ� �����ϴ�')
                        
                        
s1 = SinglyLinkedList()
s1.outputNode()

[s1.insertNode(i) for i in range(1, 6)]
s1.outputNode()

s1.deleteNode()
s1.deleteNode()
s1.deleteNode()

s1.outputNode()

s1.searchNode(5)
s1.searchNode(1)