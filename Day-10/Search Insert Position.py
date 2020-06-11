"""
Name of the problem :- Search Insert Position
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target<nums[i] or target==nums[i]:
                return i
                
            elif i==len(nums)-1:
                return len(nums)