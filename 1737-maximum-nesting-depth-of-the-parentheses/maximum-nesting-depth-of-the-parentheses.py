class Solution:
    def maxDepth(self, s: str) -> int:
        p=0
        ans=0
        for i in s:
            if i=='(':
                p+=1
                ans=max(p,ans)
            elif i==')':
                p-=1
        return ans
        