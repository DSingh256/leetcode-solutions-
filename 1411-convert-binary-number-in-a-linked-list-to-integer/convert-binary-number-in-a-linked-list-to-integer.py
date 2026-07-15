# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        a=head
        inte=0
        i=[]
        while a:
           i.append(a.val)
           a=a.next
        for j,k in enumerate(i[::-1]):
            if k==1:
                inte+=2**j
        return inte

        