class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums)==0:
            return [-1,-1]
        
        i = len(nums)//2
        if nums[i]==target:
            left = i
            right = i
            while left>-1 and nums[left]==target:
                left-=1
            while right<len(nums) and nums[right]==target:
                right+=1
            return [left+1,right-1]
        
        if nums[i]>target:
            return self.searchRange(nums[:i],target)
        
        res = self.searchRange(nums[i+1:],target)
        if res!=[-1,-1]:
            return [res[0]+i+1,res[1]+i+1]
        return res
    
"""
time: O(logn) 
space: O(logn)
"""

#         from collections import defaultdict
#         seen = defaultdict(list)

#         for i in range(len(nums)):
#             seen[nums[i]].append(i)
        
#         if target in seen.keys():
#             return [seen[target][0],seen[target][-1]]
        
#         return [-1,-1]
    
# """
# time: O(n) for looking at all elements
# space: O(n) for the dictionary
# """
