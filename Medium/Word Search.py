class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        """
        time: O(mn * 3^S) where S is the length of word, 3 because of the 3 directions we need to explore since one of the 4 will return in O(1)
        space: O(S) since the recursion happens S times
        
        """
        
        self.board = board
        
        k = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.DFS(j, i, word):
                        return True          
                    
        return False  
        
        
        
    def DFS(self, col, row, string):
        
        if string=="":
            return True
        
        # eliminate invalid inputs
        
        if row<0 or col<0 or row>=len(self.board) or col>=len(self.board[0]) or self.board[row][col]!=string[0]:
            return False
        
        
        
        self.board[row][col] = '#'
        
        if self.DFS(col-1, row, string[1:]):
            self.board[row][col] = string[0]
            return True
        
        if self.DFS(col, row-1, string[1:]):
            self.board[row][col] = string[0]
            return True
        
        if self.DFS(col+1, row, string[1:]):
            self.board[row][col] = string[0]
            return True
        
        if self.DFS(col, row+1, string[1:]):
            self.board[row][col] = string[0]
            return True
        
        self.board[row][col] = string[0]
        return False
        

            

        
                
        
            
        
        
