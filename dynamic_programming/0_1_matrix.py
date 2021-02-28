#https://leetcode.com/problems/01-matrix/solution/

from typing import List

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])

        dist = [[100 for col in range(n)] for row in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    dist[i][j] = min(dist[i][j], min(100 if i == 0 else dist[i-1][j], 100 if j == 0 else dist[i][j-1]) + 1)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    dist[i][j] = min(dist[i][j], min(100 if i == (m - 1) else dist[i+1][j], 100 if j == (n - 1) else dist[i][j+1]) + 1)

        return dist


s = Solution()

print(s.updateMatrix([[0,0,0],
 [0,1,0],
 [0,0,0]]))