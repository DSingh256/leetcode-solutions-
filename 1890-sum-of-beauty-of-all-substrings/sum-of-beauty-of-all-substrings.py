class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total_beauty = 0
        
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                
                max_f = 0
                min_f = float('inf')
                
                for f in freq:
                    if f > 0:
                        max_f = max(max_f, f)
                        min_f = min(min_f, f)
                
                total_beauty += (max_f - min_f)
                
        return total_beauty