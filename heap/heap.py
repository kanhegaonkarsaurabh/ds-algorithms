# class for implementation of a Heap structure

class Heap:
  def __init__(self, values):
    self.heap = [0] * (len(values) + 1)
    self.size = 0
    self.init_heap(values)

  def __left(self, node):
    return 2 * node

  def __right(self, node):
    return 2 * node + 1

  def init_heap(self, values):
    i = 1
    for val in values:
      self.heap[i] = val
      self.size += 1
      i += 1
    self.build_max_heap()
    print (self.heap)

  def build_max_heap(self):
    root = 1
    self.max_heapify(self.heap, root)

  def max_heapify(self, heap, node):
    l = self.__left(node)
    r = self.__right(node)
    largest = node

    if l <= self.size and self.heap[l] > self.heap[node]:
      largest = l

    if r <= self.size and self.heap[r] > self.heap[node]:
      if self.heap[l] < self.heap[r]:
        largest = r
      else:
        largest = l

    if largest != node:
      # Swap heap[node] with heap[largest]
      temp = self.heap[node]
      self.heap[node] = self.heap[largest]
      self.heap[largest] = temp
      
      # Recursively call on the sub-tree
      self.max_heapify(self.heap, largest)

