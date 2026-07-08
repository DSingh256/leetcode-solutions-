class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s)
        b=list(t)
        return sorted(b) == sorted(a)