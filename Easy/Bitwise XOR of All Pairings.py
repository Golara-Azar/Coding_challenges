class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        def xor(arr):
            res = 0
            for i in range(len(arr)):
                res^=arr[i]
            return res

        xor1 = xor(nums1)
        xor2 = xor(nums2)

        res = 0
        res^= (len(nums1)%2)*xor2
        res^= (len(nums2)%2)*xor1

    """
    time: O(m+n) where len(nums1)=m and len(nums2)=n
    space: O(1)

    """

        return res
        

        
