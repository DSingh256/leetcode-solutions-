class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=max(nums)
        b=min(nums)
        n=len(nums)
        c=[]
        for i in range(b,a+1):
            if i not in nums:
                c.append(i)
        return c        

        
        