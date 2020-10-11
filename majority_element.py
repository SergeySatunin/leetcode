# https://leetcode.com/problems/majority-element/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


input = [2,2,1,1,1,2,2]

s = Solution()
result = s.majorityElement(input)

print(result)

