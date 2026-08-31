# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        curr=head.next
        one=-1
        two=-1
        minnd=(float(inf))
        i=1
        arr=[]
        while curr.next and curr:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                if one==-1:
                    one=i
                else:
                    minnd=min(minnd,i-two)
                two =i
                  
            prev=prev.next
            curr=curr.next
            i+=1
        if one== -1 or two == one:
            return [-1, -1]
        arr.append(minnd)
        arr.append(two-one)
        return arr
