# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
        
        i = 1

        pt = head
        curr = head.val 
        nxt = head.next.val 
        
        while head.next is not None :

            if i%2==1:
                head.val = nxt
                head.next.val = curr 
                head = head.next.next 
                if head is None:
                    break
                
            else:
                curr = head.val 
                nxt = head.next.val 

            i+=1
        del curr, nxt, head
        return pt

"""
    time: O(n) going over the linked list once
    space: O(1) only allocating pointers
"""     
