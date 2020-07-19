# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, val: int, nums):
        l, r = 0, 0

        segment, sum = 0, 0

        while l <= r:
            if sum >= val:
                if segment > 0:
                    segment = min(segment, r - l)
                else:
                    segment = r - l
                l += 1
                sum -= nums[l - 1]
            elif sum < val:
                if r < len(nums):
                    sum += nums[r]
                    r += 1
                else:
                    l += 1

        return segment

nums = [2,3,1,2,4,3]
val = 7

s = Solution()
result = s.minSubArrayLen(val, nums)

print(result)