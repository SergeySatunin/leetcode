class Solution:
    def removeDuplicates(self, nums) -> int:

        l = 0
        r = 0

        if len(nums) == 0:
            return 0

        while r < len(nums):
            if nums[l] == nums[r]:
                r += 1
            else:
                l += 1
                nums[l] = nums[r]

        return l + 1

nums = [1,2,2,3,3,3,3,3,4]

s = Solution()
result = s.removeDuplicates(nums)

print(result)
