import math
class Solution:
    
    def getRow(self, rowIndex: int) -> List[int]:
        r=[]

        for k in range(rowIndex+1):
            r.append(math.comb(rowIndex,k))
        return r