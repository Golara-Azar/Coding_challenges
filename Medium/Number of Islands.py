class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        def DFS(row,col):
            
            # check validity
            if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or grid[row][col]!="1":
                return
            grid[row][col] = "0"
            
            DFS(row+1,col)
            DFS(row,col+1)
            DFS(row-1,col)
            DFS(row,col-1)
            
            return
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    num+=1
                    DFS(i,j)
        
        return num
"""
time: O(mn)
space: O(mn)

"""
