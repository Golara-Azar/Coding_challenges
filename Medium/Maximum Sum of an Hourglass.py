class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        
        import numpy
        a,b = numpy.shape(grid)

        def square(grid):
            return int(numpy.sum(grid) - grid[1][0] - grid[1][2])

        
        largest = 0
        for i in range(a-2):
            for j in range(b-2):
                M = [x[j:j+3] for x in grid[i:i+3]]
                
                largest = max(largest, square(M))
        return largest
     
"""
time: O(mn) since we have to look at all elements of the m x n grid
space: O(1) since we only use 3 x 3 extra subgrids.
"""
