class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        counts = {}
        for row in grid:
            for num in row:
                counts[num] = counts.get(num, 0) + 1
        repeating = -1
        missing = -1
        for i in range(1, n * n + 1):
            count = counts.get(i, 0)
            if count == 2:
                repeating = i
            elif count == 0:
                missing = i
        return [repeating, missing]