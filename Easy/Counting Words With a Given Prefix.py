class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        #n = len(pref)
        num = 0
        for item in words:
            if item.startswith(pref):#"".join(item[:n])==pref:
                num+=1
        
        return num

"""
time: O(nm)
space: O(1)

"""
