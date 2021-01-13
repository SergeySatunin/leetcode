# https://leetcode.com/problems/maximum-subarray/

from typing import List
import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]

        max_sum = -1 * sys.maxsize

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            max_sum = max(max_sum, dp[i])

        return max(dp)