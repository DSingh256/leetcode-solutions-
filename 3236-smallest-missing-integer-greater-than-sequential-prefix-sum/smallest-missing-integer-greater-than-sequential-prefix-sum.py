class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seq_sum=nums[0]
        for j in range(1,len(nums)):
            if nums[j] == nums[j - 1] + 1:
                seq_sum += nums[j]
            else:
                break
        num_set = set(nums)
        ans = seq_sum
        while ans in num_set:
            ans += 1
            
        return ans


        