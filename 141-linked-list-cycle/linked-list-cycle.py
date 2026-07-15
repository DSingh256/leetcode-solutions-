# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        slow =head 
        while current and current.next:
            current=current.next.next
            slow=slow.next
            if current ==slow:
                return True
                break
        return False
        
        