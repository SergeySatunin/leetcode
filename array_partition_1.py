# https://leetcode.com/problems/array-partition-i/

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        i = 0
        j = 1
        total = 0
        while j < len(nums):
            total += min(nums[i], nums[j])
            i += 2
            j += 2

        return total

input = [1,4,3,2]

s = Solution()
result = s.arrayPairSum(input)

print(result)
print()