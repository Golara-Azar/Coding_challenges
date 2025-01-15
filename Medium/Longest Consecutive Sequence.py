class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        cans = set(nums)
        res = 0
        longest = 0

        for num in cans:
            if num-1 not in cans:
                curr = num
                longest = 1
                while curr+1 in cans:
                    curr+=1
                    longest+=1
                res = max(res,longest)
        return res

        
        # n = len(nums)
        # if n<=1:
        #     return n
        

        
        # cans = sorted(list(set(nums)))

        # if len(cans)==1:
        #     return 1

        # res = 0
        # longest = 1
        
        # for i in range(1,len(cans)):
        #     if cans[i]-cans[i-1]==1:
        #         longest+=1
        #     else:
        #         res = max(longest,res)
        #         longest = 1
        
        
        # res = max(longest,res)
        # longest = 1
        
        # del cans

        return res

  """
  time:
    hash table method: O(n)
    sort method: O(nlogn)
  space: O(n) to hold the set of candidates
 


  """
