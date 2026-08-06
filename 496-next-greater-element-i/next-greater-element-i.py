class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for i in nums1:
            idx=nums2.index(i)
            found_greater = False
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > i:
                    a.append(nums2[j])
                    found_greater = True
                    break
                
            if not found_greater:
                a.append(-1)
        return a

