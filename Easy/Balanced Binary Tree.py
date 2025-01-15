# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_height(node):
            if node is None:
                return -1
            return 1+max(get_height(node.left),get_height(node.right))
        
        if root is None:
            return True
        
        if abs(get_height(root.left)-get_height(root.right))>1:
            return False
        

        return self.isBalanced(root.left) and self.isBalanced(root.right)

        """
        time: O(n) going over all the nodes
        space: O(n) for the recursive function results

        """


        
        
