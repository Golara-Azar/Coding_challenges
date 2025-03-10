class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      
        
        for num in nums:
            can = nums[abs(num)]
            if can<0:
                idx = abs(num)
                break
            
            nums[abs(num)] = -can
        
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        
        return idx

"""
time: O(n)
space: O(1)
"""
