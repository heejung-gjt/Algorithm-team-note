# -*- coding: utf-8 -*-
from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList

class StackSinglyLinked:
    def __init__(self):
        self.data = SinglyLinkedList()

    def push(self, data):
        self.data.insertNode(data)

    def pop(self):
        self.data.deleteNode()

    def empty(self):
        self.data.emptyNode()

    def peek(self):
        self.data.peekNode()

    def ouput(self):
        self.data.outputNode()
  

class StackDoublyLinked:
  def __init__(self):
    self.data = DoublyLinkedList()

  def push(self, data):
    self.data.insertNodeFront(data)

  def pop(self):
    self.data.deleteNodeFront()

  def ouput(self):
    self.data.outputNodeFront()

  def peek(self):
    self.data.peekNodeFront()  


if __name__ == "__main__":
  # st1 = StackSinglyLinked()
  st2 = StackDoublyLinked()
  st2.push('one')
  st2.push('two')
  st2.push('three')
  st2.ouput()
  print()
  print()
  st2.pop()
  st2.pop()
  print()
  st2.ouput()
  print()
  print()
  st2.peek()