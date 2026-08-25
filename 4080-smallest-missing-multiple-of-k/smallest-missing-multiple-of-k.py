class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1
        while i!=0:
            
            A=k*i
            if A not in nums:
                return A
                i=0
            else:
                i+=1
        