class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        import numpy as np
        M = [1] + [0 for i in range(high)] 
        #M[i]: number of all good strings with length i
        
        mod = 10**9+7
         
        for i in range(1,high+1):
            if i>=one:
                M[i] += M[i-one]
            if i>=zero:
                M[i]+= M[i-zero]

            M[i]%= mod

        
        return sum(M[low:])%mod
       
"""
time: O(high) 
space: O(high)
"""
