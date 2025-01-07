# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:


        if head is None:
            return head

        seen = dict()
        pointer = ListNode(head.val)
        pointer2 = pointer
        seen[head.val] = 1
        head = head.next

        while head is not None:
            if head.val in seen.keys():
                head = head.next
            else:
                seen[head.val] = 1
                pointer.next = ListNode(head.val)
                pointer = pointer.next
        return pointer2

        """
        time: O(n) going over the linked list
        space: O(n) for the new linked list

        """
                
