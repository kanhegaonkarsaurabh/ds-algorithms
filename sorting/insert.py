""" 
    Time - O(n^2)
    Space - O(1)  (in-place sort)
"""

def insertion_sort(nums):
  for k in range(1, len(nums)):         # Start from 1... to (length - 1)
    if nums[k] < nums[k-1]:
      i = k
      j = k-1
      # Loop invariant: 1 ... k-1 always is sorted

      while j >= 0 and nums[i] < nums[j]:      # Iterate from 1... to (k-1) and insert val. 
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp
        i = i - 1
        j = j - 1
  return nums

# print(insertion_sort([4, 5, 2, 1, 3]))
