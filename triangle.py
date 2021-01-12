# https://leetcode.com/problems/triangle/

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle[-1]) + 1)

        for row in triangle[::-1]:
            for i, el in enumerate(row):
                dp[i] = el + min(dp[i], dp[i + 1])

        return dp[0]



triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
s = Solution()
result = s.minimumTotal(triangle)

print(result)
