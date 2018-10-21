# Question: Remove a node in the middle (any node but the first and last) when you have access to only that node

def remove_middle_node(m_node):
  m_node.data = m_node.next.data      # Copy the value of the next Node
  m_node.next = m_node.next.next      # Move over to the next element

