class Solution:
    def reverseWords(self, s: str) -> str:
        a=[]
        a=s.split()
        a.reverse()
        return " ".join(a)