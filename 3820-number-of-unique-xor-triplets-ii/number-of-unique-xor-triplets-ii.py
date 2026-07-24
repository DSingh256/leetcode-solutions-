class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        u=(set(nums))
        n=len(set(nums))
        if n==1:
            return 1
        if n==2:
            return 2
        current_xors = {0}
        for _ in range(3):
            next_xors = set()
            for x in current_xors:
                for num in u:
                    next_xors.add(x ^ num)
            current_xors = next_xors
            
        return len(current_xors)