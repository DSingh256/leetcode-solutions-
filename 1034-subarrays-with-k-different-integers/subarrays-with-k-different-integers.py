class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def a(k:int):
            if k==0:
                return 0
            count =0 
            left=0
            n=len(nums)
            freq={}
            for right in range(n):
                a=nums[right]
                if a in freq:
                    freq[a]+=1
                else:
                    freq[a]=1
                while len(freq)>k:
                    ln=nums[left]
                    freq[ln]-=1 
                    if freq[ln]==0:
                        del freq[ln]
                    left+=1   
                window=right-left+1
                count+=window
            return count   
        return a(k)-a(k-1)
                    

        