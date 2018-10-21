class Node:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'


def create_tree():
  root = Node(4)
  root.left = Node(2)
  root.right = Node(5)
  root.left.left = Node(1)
  root.left.right = Node(3)
  root.right.right = Node(6)
 
  return root



def pre_order_iterative(root):
  stack = [root]
  visited = []

  while len(stack) > 0:
    node = stack.pop()
    visited.append(node.val)        # Current node

    if node.left is not None:
      stack.push(node.left)     # Visit the left child

    if node.right is not None:
      stack.push(node.right)    # Visit the right child

  return visited


print (pre_order_iterative(create_tree()))
