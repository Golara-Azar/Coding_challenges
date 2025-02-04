class Solution:
    def simplifyPath(self, path: str) -> str:
        
        l = path.split("/")
        stack = [""]
        for item in l:
            if item=="." or item=="":
                continue
            if item=="..":
                if len(stack)>1:
                    stack.pop()
                continue
            stack.append(item)
        
        
        if stack==[]:
            return "/"
        
        if len(stack)==1:
            return "/"+stack[0]
        
        res = "/".join(stack)
        return res
"""
time: O(nS) going over the string and splitting it, then going over each element, S is max length of element
space: O(nS)

"""
