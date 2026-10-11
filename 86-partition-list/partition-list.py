# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        s=ListNode(0)
        l=ListNode(0)
        sm=s
        la=l
        current=head
        while current:
            if current.val<x:
                sm.next=current
                sm=sm.next
            else:
                la.next=current
                la=la.next
            current=current.next
        la.next=None
        sm.next=l.next
        return s.next

