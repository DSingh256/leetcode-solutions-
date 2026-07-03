class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        remain=0
    
        st=set()
        for i in range(n):
            for j in range(i+1,n):
                past=set()
                for k in range(j+1,n):
                    remain=target-nums[i]-nums[j]-nums[k]
                    if remain in past:
                        temp = tuple(sorted([nums[i], nums[j], nums[k], remain]))
                        st.add(temp)
                    past.add(nums[k])
        return [list(quad) for quad in st]

        