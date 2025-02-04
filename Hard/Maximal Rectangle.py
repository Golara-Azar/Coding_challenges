class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        """
        time: O(m^2 n)
        space: O(mn)
        
        """
        
        row,col = len(matrix),len(matrix[0])
        
        M = [[0 for _ in range(col+1)] for _ in range(row+1)] #O(mn) space
        
        for i in range(row):  #O(mn) time
            for j in range(col):
                if matrix[i][j]=='1':
                    M[i+1][j+1] = M[i+1][j]+1
                
        
        
        max_rec = 0
        
        for i in range(1,row+1):  #O(m^2 n) time
            for j in range(1,col+1):
                max_width = M[i][j]
                max_rec = max(max_rec,max_width)
                k = 1
                while i-k>0: #O(m) time
                    max_width = min(max_width,M[i-k][j])
                    k+=1
                    max_rec = max(max_rec,max_width*k)
            
        return max_rec   
            
