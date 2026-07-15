# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c1=None
        c2=head
        while c2:
            c3=c2.next
            c2.next=c1
            c1=c2
            c2=c3
        return c1

           
