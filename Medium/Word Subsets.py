class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # len(words1) = m, each:k1 ; len(words2) = n, each:k2
        from collections import Counter
       
        

        max_ct = Counter()
        for i in range(len(words2)): #O(n)
            max_ct|=Counter(words2[i]) #O(k2)
        
        res = []
        for i in range(len(words1)): #O(m)
            if not max_ct - Counter(words1[i]): #O(k1)
                res.append(words1[i])
        
        return res

"""
time: O(nk2 + mk1)
space: O(m)

"""
