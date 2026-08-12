from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        maxx = 0
        
        for right in range(len(nums)):
            freq[nums[right]] += 1
            
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            
            maxx = max(maxx, right - left + 1)
            
        return maxx