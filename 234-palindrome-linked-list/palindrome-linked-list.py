# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        z1=head
        a=[]
        while z1:
            
            a.append(z1.val)
            z1=z1.next
        return a == a[::-1]