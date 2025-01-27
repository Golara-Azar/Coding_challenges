class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        
        def count_fives(m):
            total = 0
            if m<5:
                return 0
            while m%5==0:
                total+=1
                m//=5
            return total
        
        
        fives = 0
        for i in range(5,n+1,5):
            fives += count_fives(i)
                
        
        
        return fives
        
