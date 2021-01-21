# https://leetcode.com/problems/maximum-product-subarray/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return nums[0]

        dp_min = [1] * len(nums)
        dp_max = [1] * len(nums)

        dp_min[0] = dp_max[0] = total_max = nums[0]

        for i in range(1, len(nums)):
            dp_min[i] = min(nums[i], dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i])
            dp_max[i] = max(nums[i], dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i])

            total_max = max(total_max, dp_max[i])

        return total_max

s = Solution()

print(s.maxProduct([2, -5, -2, -4, 3]))

print()

#[2, -5, -2, -4, 3]