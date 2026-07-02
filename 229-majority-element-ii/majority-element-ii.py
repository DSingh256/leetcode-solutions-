class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[]
        mp= defaultdict(int)
        mini=(n//3)+1
        for nu in nums:
            mp[nu]+=1
            if mp[nu]==mini:
                result.append(nu)
            if len(result)==2:
                break
        return result

        