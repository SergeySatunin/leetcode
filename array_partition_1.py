# https://leetcode.com/problems/array-partition-i/

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        result = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                result += num

        return result

input = [1,4,3,2]

s = Solution()
result = s.arrayPairSum(input)

print(result)
print()
