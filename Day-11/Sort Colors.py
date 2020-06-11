"""
Name of the problem :- Sort Colors
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        L = [0, 0, 0]
        for i in range(len(nums)):
            L[nums[i]] = L[nums[i]]+1
            
        L[1] = L[0]+L[1]
        L[2] = L[1]+L[2]
                
        for j in range(L[0]):
            nums[j]=0
            
        for j in range(L[0], L[1]):
            nums[j]=1
            
        for j in range(L[1], L[2]):
            nums[j]=2