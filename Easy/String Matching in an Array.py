class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        from collections import Counter

        freq = sorted(words, key=lambda i: len(i)) #O(nlogn)
        res = [] #O(n)
        i = 0
        j = i+1
        while i<len(words)-1: #O(n)

            if freq[i] in freq[j]:
                res.append(freq[i])
                i+=1
                j = i+1
                if j==len(words):
                    break
            else:
                j+=1
                if j==len(words):
                    i+=1
                    if i<len(words)-1:
                        j = i+1
                    else:
                        break
        return res

"""
time: O(nlogn) due to sorting
space: O(n) to keep the result words
"""
