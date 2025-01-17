class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        if nums==[]: #O(1)
            return [[lower,upper]]
        
        res = []
        if lower<nums[0]: #O(1)
            res.append([lower,nums[0]-1]) #O(1)
        
        prev = nums[0]
        for i in range(1,len(nums)): #O(n)
            if nums[i]-prev>1: #O(1)
                res.append([prev+1,nums[i]-1]) #O(1)
            prev = nums[i]
            
        
        if upper!=nums[-1] and upper!=lower: #O(1)
            res.append([nums[-1]+1,upper]) #O(1)
            
        return res
    
"""
time: O(n)
space: O(n)
"""
        
