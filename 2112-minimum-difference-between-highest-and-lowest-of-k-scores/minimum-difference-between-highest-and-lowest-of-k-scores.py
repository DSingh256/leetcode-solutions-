class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        a=[]
        nums.sort()
        if len(nums)==0 or len(nums)==1:
            return 0
        for i in range(len(nums) - k + 1):

                a.append(nums[i+k-1]-nums[i])
        return min(a)
            
            
        