class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        from collections import defaultdict
        seen = defaultdict(list)

        for i in range(len(nums)):
            seen[nums[i]].append(i)
        
        if target in seen.keys():
            return [seen[target][0],seen[target][-1]]
        
        return [-1,-1]
    
"""
time: O(n) for looking at all elements
space: O(n) for the dictionary
"""
