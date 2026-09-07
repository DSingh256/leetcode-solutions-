class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        end = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            end[idx] = (sum(end) + 1) % MOD
            
        return sum(end) % MOD