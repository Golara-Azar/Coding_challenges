class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        m = s.length
        n = words.length
        k = words[0].length
        
        m>>k
        m = O(2n) based on constraints
        time: O(mnk)
        space: O(m+n)
        
        """
        
        from collections import Counter
        import re
        c = Counter(words) #O(n) time and space
        step = len(words[0])
        n = len(words)
        rule = ''
        for _ in range(step): #O(k) time and space
            rule+='.'
        
        i = 0
        idx = [] #O(m) space
        while i<len(s): #O(m) time
            
            if i+n*step>len(s):
                break
            
            while s[i:i+step] not in c:
                i+=1
                if i>len(s):
                    return idx
                
            candidate = re.findall(rule,s[i:i+n*step]) #O(k*n) time and O(n) space
            
            if Counter(candidate)==c:
                idx.append(i)
            i+=1
        
        
        return idx
            
        
        
            
            
        
        
        
