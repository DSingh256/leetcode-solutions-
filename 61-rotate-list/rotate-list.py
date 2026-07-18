# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr=head
        h=head
        c=1
        a=0
        while curr.next:
            curr=curr.next
            c+=1
        k = k % c
        if k == 0:
            return head
        curr.next=head
        kt=curr
        while c-k>a:
            a+=1
            kt=kt.next
        he=kt.next
        kt.next=None
        
        return he