# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def handle_subtree(stack,root): #T(n) = O(n)
            if root is None: #O(1)
                return stack
            stack = handle_subtree(stack,root.right) #T(n/2)
            stack.append(root.val) #O(1)
            stack = handle_subtree(stack,root.left) #T(n/2)
            return stack
        
        from collections import deque
        stack = []
        stack = handle_subtree(stack,root) 
        
        return stack[-k]
    
    """
    time: O(n)
    space: O(n)
    
    """
        
