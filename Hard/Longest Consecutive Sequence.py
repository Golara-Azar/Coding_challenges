class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        longest = 0
        for num in seen:
            if num-1 not in seen:
                streak=1
                current = num
                while current+1 in seen:
                    streak+=1
                    current+=1
                longest = max(longest,streak)
            
        return longest
        
"""
time: O(n)
space: O(n)
"""
