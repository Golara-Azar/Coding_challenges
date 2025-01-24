class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        time: O(m+n)
        space: O(1)
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        
        
        if matrix[0][0]==target:
            return True
        
        if matrix[0][0]>target:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        row = m-1
        col = 0
        
        while row>=0 and col<n:
            
            if matrix[row][col]==target:
                return True
            
            if matrix[row][col]>target:
                row-=1
            
            if matrix[row][col]<target:
                col+=1
        return False
                
        
            
        
        
            
        
