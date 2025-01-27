class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        
        def count_fives(m): #O(1), most numbers only have 1 five
            total = 0
            if m<5:
                return 0
            while m%5==0:
                total+=1
                m//=5
            return total
        
        
        fives = 0
        for i in range(5,n+1,5): #O(n)
            fives += count_fives(i)
                
        
        
        return fives
        
