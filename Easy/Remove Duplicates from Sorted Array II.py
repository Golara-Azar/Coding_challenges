class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        from collections import defaultdict
        seen = defaultdict(int)
        

        dups = 0
        i = 0
        while i<(len(nums)):
            if seen[nums[i]]>=2:
                nums[i] = float('inf')
                dups+=1
                
            else:
                seen[nums[i]]+=1
            i+=1
        nums.sort() #O(nlogn)
        return len(nums)-dups



"""
time: O(nlogn) due to sorting
space: O(n) due to the dictionary

"""

        
