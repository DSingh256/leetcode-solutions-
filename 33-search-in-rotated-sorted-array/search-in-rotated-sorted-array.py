class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        a = nums.index(target)
        return a
