class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        
        import numpy as np
        if n==2:
            
            return int(np.argmax(nums))
        
        i = n//2
        if nums[i]>max(nums[i-1],nums[i+1]):
            return i
        if nums[i]>nums[i+1]:
            return self.findPeakElement(nums[:i+1])
        else:
            return self.findPeakElement(nums[i:])+i
        
