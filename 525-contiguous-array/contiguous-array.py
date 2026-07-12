class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum={0:-1}
        maxx=0
        current=0
        for i,num in enumerate(nums):
            current+=1 if num==1 else -1
            if current in sum:
                maxx = max(maxx, i - sum[current])
            else:
                sum[current] = i
                
        return maxx



        