# Question: Partition a LinkedList around a particular value 'k' 
from LinkedList import LinkedList

def partition_list(k, ll):
  head = ll.head
  tail = ll.head

  current = ll.head
  while current:
    nextNode = current.next
    if current.value < k:
      current.next = head
      head = current
    else:
      tail.next = current
      tail = current
    current = nextNode
  ll.head = head
  tail.next = None        # If not, the list is a circular one


# ll = LinkedList()
# ll.generate(10, 0 , 99)
# print (ll)
# partition_list(ll.head.value, ll)
# print (ll)
