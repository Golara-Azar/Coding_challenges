class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        """
        O(n): time
        O(n): space
        """
        from collections import defaultdict
        seen = defaultdict(int)
        n = len(nums)
        for i in range(len(nums)): #O(n) time
            seen[nums[i]]+=1
            if seen[nums[i]]>n//2:
                return nums[i]
        
        return 
