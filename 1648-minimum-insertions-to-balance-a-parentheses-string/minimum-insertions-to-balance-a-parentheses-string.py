class Solution:
    def minInsertions(self, s: str) -> int:
        open_needed = 0
        right_needed = 0
        
        for char in s:
            if char == '(':
                right_needed += 2
                if right_needed % 2 == 1:
                    open_needed += 1     
                    right_needed -= 1
            else:  
                right_needed -= 1
                if right_needed < 0:
                    open_needed += 1     
                    right_needed += 2    
        return open_needed + right_needed