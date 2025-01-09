class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        agg = 0

        agg_all = sum(nums)
        res = 0
        for i in range(len(nums)-1):
            agg+=nums[i]
            
            if agg>=agg_all/2:
                res+=1
        return res
"""
time: O(n)
space: O(1)
"""
