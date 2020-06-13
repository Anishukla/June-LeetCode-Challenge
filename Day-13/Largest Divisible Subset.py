"""
Name of the problem :- Largest Divisible Subset
"""

def largestDivisibleSubset(nums):
    if len(nums) == 0: 
        return []
    
    elif len(nums) == 1: 
        return nums
    
    nums = sorted(nums)
    res = [[num] for num in nums]
    print(res)
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(res[i]) < len(res[j]) + 1:
                res[i] = res[j] + [nums[i]]
            print(res)
    return max(res, key=len)