class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        A=sorted(set(arr))
        b={}
        for i , val in enumerate(A):
            b[val]=i+1
        return [b[num] for num in arr]
        

