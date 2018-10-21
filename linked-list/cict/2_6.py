# Question: Check if the given ll is a Palindrome

from LinkedList import LinkedList

def reverse_list(ll):         # Use the two pointer technique of prev, ahead to reverse the list in-place
  prev = None
  ahead = None
  current = ll.head
  while current:
    ahead = current.next
    current.next = prev

    prev = current
    current = ahead
  ll.head = prev
  return ll.head

def is_palindrome(ll):
  f_iter = ll.head
  reverse_head = reverse_list(ll)
  s_iter = reverse_head

  while f_iter:
    if (f_iter.value != s_iter.value):
      return False
    f_iter = f_iter.next
    s_iter = s_iter.next

  return True


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(2)
ll.add(1)

print (is_palindrome(ll))

