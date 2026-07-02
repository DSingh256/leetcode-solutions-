class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_count = {0: 1}
        
        for num in nums:
            prefix_sum += num
            remove = prefix_sum - k
            
            if remove in prefix_sum_count:
                count += prefix_sum_count[remove]
            
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1
            
        return count