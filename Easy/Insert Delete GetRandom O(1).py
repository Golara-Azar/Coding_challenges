class RandomizedSet:
    """
    O(1): time
    O(n): space

    """

    def __init__(self):
        from collections import defaultdict
        self.disk = defaultdict(int)

    def insert(self, val: int) -> bool:
        if self.disk[val]>0:
            return False
        self.disk[val] += 1
        return True

    def remove(self, val: int) -> bool:
        flag = self.disk[val]==0
        self.disk[val] = 0
        return not flag
        

    def getRandom(self) -> int: 
        import numpy.random as random
        c = random.choice([x for x,y in self.disk.items() if y>0])
        return int(c)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
