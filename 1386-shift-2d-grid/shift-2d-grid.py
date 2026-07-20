class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        a=grid
        m=len(grid)
        n=len(grid[0])
        k=k%(m*n)
        if k == 0:
            return grid
        listt=[]
        for row in grid:
            for val in row:
                listt.append(val)
        shift=listt[-k:]+listt[:-k]
        new=[]
       
        for i in range(m):
            start = i * n
            end = start + n
            new.append(shift[start:end])
        return new   
