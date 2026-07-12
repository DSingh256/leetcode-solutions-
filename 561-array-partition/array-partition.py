class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        a=sorted(nums)
        i=0
        n=len(nums)
        summ=0
        while i<n:
            summ+=a[i]
           
            i+=2
            
        return summ




        