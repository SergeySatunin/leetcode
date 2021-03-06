# https://leetcode.com/problems/unique-paths-ii/
from typing import List

class Solution:
    def __init__(self):
        self.cache = {}
        self.obstacleGrid = None

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.obstacleGrid = obstacleGrid
        self.cache['1_1'] = 1 if obstacleGrid[0][0] == 0 else 0
        return self.uniquePaths(len(obstacleGrid), len(obstacleGrid[0]))

    def uniquePaths(self, m: int, n: int) -> int:
        k = str(m)+'_'+str(n)

        if k in self.cache:
            return self.cache[k]

        if self.obstacleGrid[m - 1][n - 1] == 1:
            self.cache[k] = 0
            return self.cache[k]

        from_top = 0 if m - 1 < 0 else self.uniquePaths(m - 1, n)
        from_left = 0 if n - 1 < 0 else self.uniquePaths(m, n - 1)
        result = from_top + from_left

        self.cache[k] = result

        return self.cache[k]


s = Solution()
result = s.uniquePathsWithObstacles([[0,1],[0,0]])

print(result)