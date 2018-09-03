import node

class LinkedList:
  def __init__(self, head):
    self.size = 0
    self.head = node.Node(head)
    self.size += 1

  def append(self, val):
    iter = self.head
    while iter.next != None:
      iter = iter.next
    iter.next = node.Node(val)

  def print(self):
    iter = self.head
    while iter != None:
      print (iter.data)
      iter = iter.next
