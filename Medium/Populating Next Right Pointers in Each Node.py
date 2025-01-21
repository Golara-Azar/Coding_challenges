"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if root is None:
            return None
        self.connect(root.left) #T(n/2)
        self.connect(root.right) #T(n/2)
        
        pt_left = root.left #O(1)
        pt_right = root.right #O(1)
        while pt_left: #O(log n)
            pt_left.next = pt_right #O(1)
            pt_left = pt_left.right #O(1)
            pt_right = pt_right.left #O(1)
        
        return root
    
    """
    time:
    T(n) = 2T(n/2) + O(log n)
    T(n) = O(log n)
    space:
    O(1)
    
    """
