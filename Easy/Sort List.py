# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        pt = head
        vals = []
        while pt:
            vals.append(pt.val)
            pt = pt.next

        vals.sort()
        pt = head
        for item in vals:
            pt.val = item
            pt = pt.next

        return head

"""
time: O(nlogn) due to sorting
space: O(n) for the additional list

"""
