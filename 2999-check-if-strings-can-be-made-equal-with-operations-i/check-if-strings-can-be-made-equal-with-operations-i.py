class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        for i in range(2):
            j=i+2
            if s1[i]==s2[i]:
              continue
            elif s1[j]==s2[i] and s1[i]==s2[j]:              
                  s1[i], s1[j] = s1[j], s1[i]
                
        if s1==s2:
            return True
        else:
            return False
    
        