class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:

        """"
        time: O(n)
        space: O(n)


        """"
        
        if len(s)<3:
            return []
        
        
        res = []
        
        i = 0
        while i<len(s):
            
            curr = s[i]
            start = i
            
            
            while s[i]==curr:
                i+=1
                if i==len(s):
                    break
            end = i-1
            
            if end-start>=2:
                res.append([start,end])
        return res
            
        
        
            
        
        
            
