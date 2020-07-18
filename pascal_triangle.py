# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int):

        if numRows == 0:
            return []

        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1,1])
            else:
                row = []
                for j in range(i + 1):
                    if j == 0 or j == i:
                        row.append(1)
                    else:
                        row.append(result[i-1][j-1] + result[i-1][j])
                result.append(row)

        return result


s = Solution()
result = s.generate(5)

print(result)