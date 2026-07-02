import copy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        o=len(matrix[0])
        m= copy.deepcopy(matrix)
        for i in range(n):
            for j in range(o):
                if m[i][j]==0:
                    for z in range(o):
                        matrix[i][z]=0
                    for zi in range(n):    
                        matrix[zi][j]=0
        return matrix