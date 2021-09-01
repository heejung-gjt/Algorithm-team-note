
from doubly_linked_list import DoublyLinkedList


class Queue:
  def __init__(self):
    print('큐 -> 이중 링크드 리스트 구현\n')
    self.data = DoublyLinkedList()

  def enqueue(self, data):
    self.data.insertNodeFront(data)

  def dequeue(self):
    self.data.deleteNodeBack()
  
  def peek(self):
    self.data.peekNodeBack()
  
  def output(self):
    self.data.outputNodeFront()


if __name__=="__main__":
  que = Queue()
  que.enqueue(1)
  que.enqueue(2)
  que.enqueue(3)
  que.enqueue(4)
  que.output()
  print()
  print()
  que.dequeue()
  print()
  que.output()
  print()
  print()
  que.dequeue()
  print()
  que.output()
  print()
  print()
  que.dequeue()
  print()
  que.output()
  print()
  print()
  que.peek()
  print()