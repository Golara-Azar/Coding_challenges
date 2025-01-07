# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
        if k==0:
            return head
        
        vals = []
        while head is not None:
            vals.append(head.val)
            head = head.next
        
        k%=len(vals)
        vals = vals[-k:]+vals[:-k]

        while vals!=[]:
            head = ListNode(vals.pop(),head)
        
        return head

"""
time: O(n) for going over all the list
space: O(n) for the values list

"""
