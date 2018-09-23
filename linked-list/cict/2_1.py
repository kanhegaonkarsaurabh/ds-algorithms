# Remove dups: Write code to remove the duplicates from an unsorted linked-list

from list import LinkedList
from node import Node

def remove_dups(head):
  buffer = set()
  iter = head
  while iter.next != None:
    if iter.next.data not in buffer:
      buffer.add(iter.next.data)
      iter = iter.next
    else:
      temp = iter.next
      iter.next = temp.next


def remove_dups_no_buffer(head):
  iter = head
  while iter != None:
    current = iter
    while current.next != None:
      if iter.data == current.next.data:
        temp = current.next
        current.next = temp.next
      else:
        current = current.next
    iter = iter.next

def main():
  list = LinkedList(1)
  list.append(2)
  list.append(3)
  list.append(4)
  list.append(5)
  list.append(2)
  list.append(4)
  list.append(6)

  list.print()
  remove_dups(list.head)
  list.print()

if __name__ == "__main__":
  main()
