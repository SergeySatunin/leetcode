# https://leetcode.com/problems/contains-duplicate/

from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums) -> bool:
        unique = defaultdict(int)
        status = False

        for i in nums:
            if i in unique.keys():
                status = True
                break
            else:
                unique[i] = 1

        return status

input = []
s = Solution()
result = s.containsDuplicate(input)

print(result)