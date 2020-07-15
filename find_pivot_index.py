# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        running_total = 0
        result = -1

        for i in range(len(nums)):
            if total - nums[i] - running_total == running_total:
                result = i
                break
            running_total += nums[i]

        return result

nums = [1,1,1,1,3,2,1,1]
s = Solution()
result = s.pivotIndex(nums)

print(result)