class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        n=len(nums)
        prefixgcd=[]
        mx=float('-inf')
        for i in range(n):
            mx=max(mx,nums[i])
                
            prefixgcd.append(gcd(nums[i],mx))
        prefixgcd=sorted(prefixgcd)
        j=n-1
        i=0
        sum=0
        while i<j:
            sum=sum+gcd(prefixgcd[i],prefixgcd[j])
            i+=1
            j-=1
        return sum
            
        