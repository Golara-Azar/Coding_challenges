# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        def is_leaf(root):
            if root is None:
                return False
            return (root.left is None) and (root.right is None)
            
        
        stack = [root]
        res = 0
        while len(stack)>0:
            curr = stack.pop()
            
            if is_leaf(curr.left):
                res+=curr.left.val
            
            if curr.right:
                stack.append(curr.right)
            
            if curr.left:
                stack.append(curr.left)
            
        return res
        
