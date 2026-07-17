from typing import List
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
            
        F = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            count_multiples = 0
            for j in range(i, max_val + 1, i):
                count_multiples += freq[j]
            F[i] = count_multiples * (count_multiples - 1) // 2
            
        exact_gcd = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            exact_gcd[i] = F[i]
            for j in range(2 * i, max_val + 1, i):
                exact_gcd[i] -= exact_gcd[j]
                
        prefix = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix[i] = prefix[i - 1] + exact_gcd[i]
            
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix, q)
            ans.append(idx)
            
        return ans