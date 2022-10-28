# https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/

from typing import List

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) <= 1:
            return 0

        i = 0
        j = 1
        total = 0
        while i < len(s) and j < len(s):
            if s[i] != s[j]:
                if j > i:
                    total += max(cost[i:j])
                    i = j
                else:
                    i += 1
            else:
                j += 1

        if j > i:
            total += max(cost[i:j])

        return sum(cost) - total






s = Solution()
print(s.minCost(s = "aabaa", cost = [1,2,3,4,1]))