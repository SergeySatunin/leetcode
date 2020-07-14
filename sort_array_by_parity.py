# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums):

        slow = 0

        for fast in range(len(nums)):
            if nums[fast] % 2 == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        return nums

nums = [3, 1, 0, 2, 4, 7]

s = Solution()
s.sortArrayByParity(nums)

print(nums)