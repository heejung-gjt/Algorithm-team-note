# -*- coding: utf-8 -*-
class Node:
    def __init__(self, v, n = None):
        self.value = v
        self.next = n


class SinglyLinkedList:
            
    def __init__(self):
        self.head = None

    def insertNode(self, data):
        if self.head is None:
            print('추가되는 데이터>>>', data)
            self.head = Node(data)
        else:
            print('추가되는 데이터>>>', data)
            self.head = Node(data, self.head)

    def outputNode(self):
        if self.head is None:
            print('출력할 노드가 없습니다')
            print()
            return
        else:
            link = self.head
            print()
            print('출력되는 노드>>>>', end= ' ')
            while link:
                print(link.value, end=' ')
                link = link.next
            print()
            print()
            
    def deleteNode(self):
        if self.head is None:
            print('삭제할 노드가 없습니다')
            return
        else:
            print('삭제되는 노드 : ', self.head.value)
            self.head = self.head.next

    def searchNode(self, data):
        if self.head is None:
            print('찾을수 있는 노드가 없습니다')
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
            print(f'찾으시는 {data} 데이터는 없습니다')

    def emptyNode(self):
        if self.head is None:
            print('해당 노드는 비워져 있습니다')
            return True
        else:
            print('해당 노드는 존재합니다')
            return False

    def peekNode(self):
        if self.head is None:
            print('노드가 존재하지 않습니다')
        else:
            return print(f'현재 head에 존재하는 데이터는 {self.head.value} 입니다')
                        
                        
# s1 = SinglyLinkedList()
# s1.outputNode()

# [s1.insertNode(i) for i in range(1, 6)]
# s1.outputNode()

# s1.deleteNode()
# s1.deleteNode()
# s1.deleteNode()

# s1.outputNode()

# s1.searchNode(5)
# s1.searchNode(1)

# s1. peekNode()