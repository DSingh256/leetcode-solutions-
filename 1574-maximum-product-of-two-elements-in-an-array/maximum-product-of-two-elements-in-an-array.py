class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=sorted(nums)
        n=len(nums)
        a1=a[n-1]
        a2=a[n-2]
        for i in range(n):
            if nums[i]==a1:
                k=i
            if nums[i]==a2:
                j=i
        return (nums[k]-1)*(nums[j]-1)

        