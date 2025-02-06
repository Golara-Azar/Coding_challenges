class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if k==len(num):
            return "0"
        
        stack = []
        
        for item in num: 
        
            while stack and k and item<stack[-1]:
                stack.pop()
                k-=1
            stack.append(item)
        
        if k:
            stack = stack[:-k]
            
        
        
        if stack:
            res = "".join(stack).lstrip('0')
            
            return res or "0"
        
        return "0"
        
"""
time: O(n) going over each word
space: O(n) for the stack

"""
        
