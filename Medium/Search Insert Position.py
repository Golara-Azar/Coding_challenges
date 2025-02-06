class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        time: O(logn)
        space: O(1)
        
        """
        
        left = 0
        right = len(nums)-1
        
        while left<=right:
            idx = (left+right)//2
            if nums[idx]==target:
                return idx
            if target<nums[idx]:
                right-=1
            else:
                left+=1
        
        return left
        
#         if target in nums:
#             return nums.index(target)
        
#         n = len(nums)
#         if n==0:
#             return 0
        
#         if n==1:
#             if target>nums[0]:
#                 return 1
#             else:
#                 return 0
        
        
#         if n==2:
#             if target>nums[1]:
#                 return 2
#             if target<=nums[0]:
#                 return 0
#             return 1
        
        
#         idx = n//2
#         if nums[idx]==target:
#             return idx
        
#         if nums[idx-1]>target:
#             return self.searchInsert(nums[:idx-1], target)
#         if nums[idx]<target:
#             return idx+1 + self.searchInsert(nums[idx+1:], target)
        
#         return idx
