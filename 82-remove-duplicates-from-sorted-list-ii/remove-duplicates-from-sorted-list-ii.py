class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        s = set()
        seen = set()
        curr = head
        
        while curr:
            if curr.val in seen:
                s.add(curr.val)
            else:
                seen.add(curr.val)
            curr = curr.next

        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        
        while curr:
            if curr.val in s:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
                
        return dummy.next