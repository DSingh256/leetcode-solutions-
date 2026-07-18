class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
            
        dummy = ListNode(0, head)
        prev = dummy
        
        while n >= k:
            kth = prev
            for i in range(k):
                kth = kth.next
                
            groupNext = kth.next
            
            curr_prev = groupNext
            curr = prev.next
            
            for _ in range(k):
                temp = curr.next
                curr.next = curr_prev
                curr_prev = curr
                curr = temp
                
            temp = prev.next
            prev.next = kth
            prev = temp
            
            n -= k
            
        return dummy.next