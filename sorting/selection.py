"""
    Time - O(n^2)
    Space - O(1) (in-place sort)
"""

def selection_sort(nums):
    for i in range(0, len(nums) - 1):
        min = i
        for j in range(i+1, len(nums) - 1):
            if nums[j] < nums[min]:
                temp = nums[min]
                nums[min] = nums[j]
                nums[j] = temp
    return nums
