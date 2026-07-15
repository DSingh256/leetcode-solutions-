# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1=headA
        c2=headB
        while c1!=c2:
            if c1 is None:
                c1=headB
            else:
                c1=c1.next
            if c2 is None:
                c2=headA
            else:
                c2=c2.next
        return c1
            
       
            

        
        