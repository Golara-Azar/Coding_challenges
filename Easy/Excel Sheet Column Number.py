class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for letter in list(columnTitle):
            num *=26
            num += ord(letter)-ord('A')+1
        return num
"""
time: O(n)
space: O(1)
"""
