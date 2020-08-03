# https://leetcode.com/problems/rotate-image/
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Reverse the list
        matrix.reverse()

        # Then transpose the matrix
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


m = [[1,2,3],[4,5,6],[7,8,9]]

s = Solution()
s.rotate(m)

print(m)