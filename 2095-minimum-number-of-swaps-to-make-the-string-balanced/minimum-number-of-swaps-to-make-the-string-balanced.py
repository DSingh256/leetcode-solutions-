class Solution:
    def minSwaps(self, s: str) -> int:
        a=list(s)
        left=0
        right=len(s)-1
        balance=0
        swap=0
        while left<right:
            if a[left]=='[':
                balance+=1
            else:
                balance-=1
            if balance<0:
                while right>left and a[right]!='[':
                    right-=1
                a[left],a[right]=a[right],a[left]
                swap+=1
                balance=1
            left+=1
        return swap