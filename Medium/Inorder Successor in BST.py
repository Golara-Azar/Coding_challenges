# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        
        prev = [] #O(n) space
        while root: #O(logn) in average and O(n) in worst case
            if root.val==p.val:
                break
                    
            elif root.val<p.val:
                
                root = root.right
                
            elif root.val>p.val:
                
                prev.append(root)
                root = root.left
            
        
        if root.right:
            
            root = root.right
            if not root.left:
                return root
            
            while root.left:
                root = root.left
                v = root
            return v
        
        for i in range(1,len(prev)+1): #O(n)
            
            if p.val < prev[-i].val:
                
                return prev[-i]
            
                
            
        return None
    
"""
O(n): time
O(n): space
"""
        
