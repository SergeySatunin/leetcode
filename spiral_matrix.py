# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix):

        result = []

        n = len(matrix)
        if n == 0:
            return matrix

        m = len(matrix[0])
        top = 0
        left = 0
        bottom = n - 1
        right = m - 1

        # 0 - left to right, 1 - top to bottom, 2 - right to left, 3 - bottom to up
        direction = 0

        while top <= bottom and left <= right:
            if direction == 0:
                for i in range(left, right + 1):
                    result.append(matrix[top][i])
                top += 1
                direction = 1
            elif direction == 1:
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1
                direction = 2
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
                direction = 3
            elif direction == 3:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
                direction = 0

        return result


matrix = \
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

s = Solution()
result = s.spiralOrder(matrix)

print(result)