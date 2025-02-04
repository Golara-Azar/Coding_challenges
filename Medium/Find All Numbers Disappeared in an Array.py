class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # return list(set(range(1,len(nums)+1)) - set(nums)) # O(n) both time and space
        
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            if nums[idx]>0:
                nums[idx]*=(-1)
            
        res = []
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res
  """
time: O(n)
space: O(1) not counting output list

  """
