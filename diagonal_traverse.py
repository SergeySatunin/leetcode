# https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, matrix):
        result = []
        n = len(matrix)

        if n == 0:
            return matrix

        m = len(matrix[0])

        for row_position in range(n):
            for column_position in range(m):

                if row_position > 0 and column_position != m - 1:
                    continue

                i = row_position
                j = column_position
                nums = []

                while i >= 0 and i < n and j >= 0 and j < m:
                    nums.append(matrix[i][j])
                    i += 1
                    j -= 1

                if (column_position + row_position) % 2 != 0:
                    result.extend(nums)
                else:
                    result.extend(reversed(nums))

        return result


input = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

s = Solution()
print(s.findDiagonalOrder(input))
