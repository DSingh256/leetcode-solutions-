class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        from itertools import groupby
        
        total_ones = s.count('1')
        t = '1' + s + '1'
        
        groups = [len(list(group)) for char, group in groupby(t)]
        
        max_delta = 0
        
        for i in range(2, len(groups) - 1, 2):
            delta = groups[i - 1] + groups[i + 1]
            if delta > max_delta:
                max_delta = delta
                
        return total_ones + max_delta