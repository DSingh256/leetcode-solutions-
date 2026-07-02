class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxx = 0
        num_set = set(nums)
        
        for i in num_set:
            if i - 1 not in num_set:
                j = i
                c = 0
                while j in num_set: 
                    j += 1
                    c += 1
                maxx = max(maxx, c)
                
        return maxx