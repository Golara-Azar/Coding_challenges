class Vector2D:

    def __init__(self, vec: List[List[int]]):
        
        
        self.vector = []
        for row in vec:
            for col in row:
                self.vector.append(col)
            
        self.pt = -1
        

    def next(self) -> int:
        self.pt+=1
        
        return self.vector[self.pt]
        
        

    def hasNext(self) -> bool:
        
        return self.pt<len(self.vector)-1
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
